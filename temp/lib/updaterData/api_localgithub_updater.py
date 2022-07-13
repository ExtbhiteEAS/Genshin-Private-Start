import os
import zipfile
import json
import wget

# // TODO: make updater class and etc.

with open("temp\lib\\updaterData\\api-localgithub-config.json", "r", encoding="utf-8") as updater_config:
    UpdaterManifestConfig = json.load(updater_config)

class UpdaterManifest:

    def __init__(self):
        self.updaterManifestPath = os.path.isdir("updater-build")
        #self.jsonGetVersionGitHub = json.loads(requests.get(UpdaterManifestConfig["api-updater"]["versionUpdaterCheck"]))

    def UpdaterManager(self):
        if self.updaterManifestPath == True:
            print("[WARN] In beta stade.\n[INF] Downloading zip file...")
            downloadUrl = "https://github.com/ExtbhiteEAS/Genshin-Private-Start/archive/refs/heads/main.zip"
            wget.download(downloadUrl)
            print("\n[INF] Downloaded zip file.")
            os.system("move Genshin-Private-Start-main.zip updater-build/")
            print("[INF] Moved zip file to build...")
            input("[INF] Confirm downloaded zip file to press [Enter] :: ")
            zip_file = zipfile.ZipFile("updater-build\Genshin-Private-Start-main.zip", "r")
            zip_file.extractall()
            zip_file.close()
        if self.updaterManifestPath == False:
            print("[WARN] I'm can't find build folder.")
