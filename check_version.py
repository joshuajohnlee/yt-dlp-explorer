import subprocess
import requests
import json

def check_ver(path_name):
    if path_name.is_file():
        print("YT-DLP was found. Checking version.")

    installed_version = subprocess.getoutput(".\\bin\\yt-dlp.exe --version")

    latest_ver = requests.get("https://api.github.com/repos/yt-dlp/yt-dlp/releases", "Accept: application/vnd.github+json")

    latest_ver_content = json.loads(latest_ver.content)

    latest_ver_number = latest_ver_content[0]['tag_name']

    if installed_version == latest_ver_number:
        print("Versions match")
    else:
        print("Version mismatch detetcted. Please ensure your yt-dlp.exe is up to date.")