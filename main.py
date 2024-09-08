from pathlib import Path
from check_version import check_ver 

# Check yt-dlp is found
yt_exec = Path(".\\bin\\yt-dlp.exe")
check_ver(yt_exec)