import json
import os

args = []

print("""Options and values:
* setlang; -russian -english
* pycache_cleaner; -true | -false
* console; -exit
""")

while True:
    command_option = input("<settings> [INF] Option :: ")
    if command_option == "setlang":
        args.append(command_option)
        args.append(input(f"<settings> [INF] Select value for option '{command_option}' :: "))

    if command_option == "pycache_cleaner":
        args.append(command_option)
        args.append(input(f"<settings> [INF] Select value for option '{command_option}' :: "))

    if command_option == "console":
        args.append(command_option)
        args.append(input(f"<settings> [INF] Select value for option '{command_option}' :: "))

    match args:
        case ["setlang", arg]:
            print(f"<settings> [DE] debug: {arg}")

            if arg == "-russian":
                with open("lib/app-settings.json", "r", encoding="utf-8") as settings_json:
                    settings_option = json.load(settings_json)

                if settings_option["main-application"]["localisation"] == "local_russian":
                    print("<settings> [INF] Этот язык был итак заменён на Русский.")
                else:
                    settings_option["main-application"]["localisation"] = "local_russian"

                    with open("lib/app-settings.json", "w", encoding="utf-8") as settings_json:
                        json.dump(settings_option, settings_json, indent=4)

                    success_local_set = settings_option["main-application"]["localisation"]
                    print(f"<settings> [INF] Успешно был заменён язык на Русский. Status: {success_local_set}")
                args.clear()

            if arg == "-english":
                with open("lib/app-settings.json", "r", encoding="utf-8") as settings_json:
                    settings_option = json.load(settings_json)

                if settings_option["main-application"]["localisation"] == "local_english":
                    print("<settings> [INF] This language already changed to English.")
                else:
                    settings_option["main-application"]["localisation"] = "local_english"

                    with open("lib/app-settings.json", "w", encoding="utf-8") as settings_json:
                        json.dump(settings_option, settings_json, indent=4)

                    success_local_set = settings_option["main-application"]["localisation"]
                    print(f"<settings> [INF] Successfully changed language to English. Status: {success_local_set}\n<settings> [WARN] This language in current developemt status, only russian. :(")
                args.clear()

        case ["pycache_cleaner", arg]:
            print(f"<settings> [DE] debug: {arg}")
            if arg == None:
                print(f"<settings> [INF] Please select option '{command_option}'")
            if arg == "-true":
                args.clear()

        case ["console", arg]:
            print(f"<settings> [DE] debug: {arg}")
            if arg == None:
                print(f"<settings> [INF] Please select option '{command_option}'")
            if arg == "-exit":
                args.clear()
                os._exit(0)

        case _:
            print(f"<settings> [INF] This option({command_option}) does not exist.")