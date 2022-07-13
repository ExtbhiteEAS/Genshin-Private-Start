## Copyright [2022-2024] [Extbite]
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

from lib import systemapp_package
import os, json, time

with open("temp\lib\localisation\local_russian.json", "r", encoding="utf-8") as russian_json:
    russian_lang = json.load(russian_json)

def main(language: str):
    systemTemp = systemapp_package.FunctionsSystem(language=language)
    if language == "local_russian":
        print(russian_lang["1_thanks_for_installing"])
    while True:
        commandInput = input(f"<0> :: ")
        match commandInput:

            case "start --server":
                systemTemp.ServerStart()
            
            case "start --genshin":
                systemapp_package.FunctionsSystem.GenshinApplicationStart()

            case "settings":
                os.system("cd temp\ && rename app-bat-function-settings.frmt app-bat-function-settings.bat && start app-bat-function-settings.bat")
                time.sleep(1.1)
                os.system("cd temp\ && rename app-bat-function-settings.bat app-bat-function-settings.frmt")

            case "exit":
                print(f"[INF] Exited from console with 0 status.")
                os._exit(0)

            case _:
                if commandInput == "start":
                    print(f"[INF] Command \"{commandInput}\" hasn't value. Please type this command with any values.")

if __name__ == "__main__":
    with open("temp\lib\\app-settings.json", "r", encoding="utf-8") as config_json:
        config = json.load(config_json)

    pycache_clear = config["main-application"]["pycache-clear"]

    if pycache_clear == True:
        os.system("del temp\lib\__pycache__\systemapp_package.cpython-310.pyc")
        os.system("RMDIR temp\lib\__pycache__")
    if pycache_clear == False:
        pass

    lang = config["main-application"]["localisation"]
    main(language=lang)
