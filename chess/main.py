from colorama import init, Fore, Back, Style, Cursor
import random
import os

print("Chess!")

init(autoreset = True)

board = []
rows = []

white_pieces = {
    "king": "♔",
    "queen": "♕",
    "rook": "♖",
    "bishop": "♗",
    "knight": "♘",
    "pawn": "♙"
}
black_pieces = {
    "king": "♚",
    "queen": "♛",
    "rook": "♜",
    "bishop": "♝",
    "knight": "♞",
    "pawn": "♟"
}

for file in range(8):
    for rank in range(8):
        isLightSquare = (file + rank) % 2 != 0
        # print(isLightSquare)
        
        if isLightSquare:
            board.append(Back.GREEN + Fore.WHITE + " " + white_pieces.get("pawn") + " ")
        else:
            board.append(Back.BLUE + Fore.BLACK + " " + white_pieces.get("pawn") + " ")

row = 0
for i in range(8):
    t = ""
    for k in range(row*8, (row*8) + 8):
        print(k)
        t += board[k]
    rows.append(t)
    row += 1
    
for i in rows:
    print(i)
