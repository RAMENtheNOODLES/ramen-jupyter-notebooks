from colorama import init, Fore, Back, Style, Cursor
import random
import os

print("Chess!")

board = []
rows = []

for file in range(8):
    for rank in range(8):
        isLightSquare = (file + rank) % 2 != 0
        print(isLightSquare)
        
        if isLightSquare:
            board.append(Fore.WHITE + "▀")
        else:
            board.append(Fore.BLUE + "▀")

row = 1
for i in range(len(board)):
    pass
