from colorama import init, Fore, Back, Style, Cursor
import random
import re

print("pixel art!")

width, height = 21, 19

init(autoreset=True)

colors = {
  "w": Fore.WHITE,
  "b": Fore.BLACK,
  "r": Fore.RED,
  "y": Fore.YELLOW,
  "g": Fore.GREEN,
  "m": Fore.MAGENTA,
  "u": Fore.BLUE,
  "c": Fore.CYAN
}

def readFromFile(filename):
    f = open(filename, "r")
    return f.read()
    
lines = readFromFile("pixelart.txt").split("\n")

canvas = ""

for i in lines:
    # print(*re.split("(\d*\w)", i))
    for k in re.split("(\d*\w)", i):
        if k in ["", " "]:
            continue
        print(k)
        #print(*list(k))
        l = list(k)
        print(*l)
        print(l[0])
        for j in range(0, int(l[0]) if len(l) == 2 else int(l[0] + l[1])):
            canvas += l[1] if len(l) == 2 else l[2]
    canvas += "\n"

for i in colors.keys():
    canvas.replace(i, colors[i] + "□")
    
print(canvas)
pixel = "□"
"""
canvas = ""

for i in range(width):
    for k in range(height):
        canvas += pixel + " "
    canvas += "\n"

print(canvas)
"""
