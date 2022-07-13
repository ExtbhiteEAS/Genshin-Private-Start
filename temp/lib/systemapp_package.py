import json
import time
import os

with open("temp\lib\\app-configuration.json", "r", encoding="utf-8") as config:
    app_config = json.load(config)

with open("temp\lib\localisation\local_russian.json", "r", encoding="utf-8") as russian_json:
    russian_lang = json.load(russian_json)

class FunctionsSystem:

    def __init__(self, language: str):
        self.language = language

    def ServerStart(self):

        if self.language == "local_russian":
            print(russian_lang["2_starting_fiddler"])
            os.system(app_config["main-application-settings"]["config-startup-command"]["config-start-fiddler"])
            time.sleep(1.0)
            print(russian_lang["3_started_fiddler"])

            jar_file_name = app_config["main-application-settings"]["config-grasscutter-start-patcher"]
            print(russian_lang["5_starting_jar_package"])
            os.system(f"java -jar {jar_file_name}")

    def GenshinApplicationStart():
        print("[INF] Starting Genshin Impact...")
        os.system(app_config["main-application-settings"]["config-startup-command"]["config-start-genshin"])
        print("[INF] Started Genshin Impact...")