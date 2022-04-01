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
    isKingRow = file in [0, 7]
    isPawnRow = file in [1, 6]
    onWhiteSide = file in [0, 1]
    for rank in range(8):
        isLightSquare = (file + rank) % 2 != 0
        # print(isLightSquare)
        
        tile = " "
        color = ""
        
        if onWhiteSide:
            color = Fore.WHITE
        else:
            color = Fore.BLACK
        
        if isPawnRow:
            tile = white_pieces["pawn"]
        if isKingRow:
            if rank in [0, 7]:
                tile = white_pieces["rook"]
            if rank in [1, 6]:
                tile = white_pieces["knight"]
            if rank in [2, 5]:
                tile = white_pieces["bishop"]
            if rank is 3:
                tile = white_pieces["queen"]
            if rank is 4:
                tile = white_pieces["king"]
        
        if isLightSquare:
            board.append(Back.GREEN + color + " " + tile + " ")
        else:
            board.append(Back.BLUE + color + " " + tile + " ")

row = 0
for i in range(8):
    t = ""
    for k in range(row*8, (row*8) + 8):
        # print(k)
        t += board[k]
    rows.append(t)
    row += 1
    
for i in rows:
    print(i)
