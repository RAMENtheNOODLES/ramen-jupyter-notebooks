from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time

init(autoreset=True)

curdir = os.getcwd()

colors = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
}

class Plugins:
    def __init__(self):
        pass

    def run_plugin(self, plugin_name, linenum=0):
        f = open(f"{curdir}/plugins/{plugin_name}", "r")

        lines = f.read().split("\n")

        for i in lines:
            # print(i)

            if i.__contains__("`"):
                continue
            if re.match("text, (\w*): ", i):
                color = get_colors(i.split(", ")[1].split(":")[0])
                # print(i.split(", ")[1].replace(":", ""))
                print(color + i.split(": ")[1])
                continue
            if i.__contains__("text"):
                print(i.split("text: ")[1])
            if i.__contains__("prompt"):
                choices = i.split("prompt, (")[1].split(")")[0]
                destinations = i.split("> (")[1].split(")")[0].split(", ")
                after_text = i.split(": ")[1]
                # print(choices)
                # print(destinations)

                print(f"Please select from one of these choices: ({choices})")

                while True:
                    choice = input(">")

                    if choice in choices.split(", "):
                        for k in range(len(lines)):
                            if lines[k] == f"> {choice.lower()}":
                                pass
                        return

                    print("That is not a valid option...")
                    continue

                print(after_text)
            if i.__contains__("wait"):
                time.sleep(int(i.split("wait, ")[1].split(":")[0]))
                print(i.split(": ")[1])
            if i.__contains__("goto > "):
                d_chapter = i.split("goto > ", "")[1].split(":")[0] + ".txt"
                d = i.split(": ")[1] + ".txt"
                read_story(d_chapter, d)
                return
            if i.__contains__("goto: "):
                read_story(chapter, i.split("goto: ")[1] + ".txt")
                return
