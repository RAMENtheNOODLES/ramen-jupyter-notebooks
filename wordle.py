from colorama import init, Fore, Back, Style, Cursor
import os

max_x, max_y = os.get_terminal_size()

init(autoreset = True)

pos = lambda y, x: Cursor.POS(x, y)

print(Fore.GREEN + "Wordle in Python!")
print(f"Max X: {max_x}\nMax Y: {max_y}")
