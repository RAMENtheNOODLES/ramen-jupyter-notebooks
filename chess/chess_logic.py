import re
from colorama import init, Fore, Back, Style, Cursor

class logic:
    def __init__(self):
        self.starting_pos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.white_pieces = {
            "king": "♔",
            "queen": "♕",
            "rook": "♖",
            "bishop": "♗",
            "knight": "♘",
            "pawn": "♙"
        }
    
    def FENtoBoard(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        notation = FEN
        temp = notation.split("/")
        ranks = []
        player = re.split(" ([wb]) ", notation)[1] # notation.split(" ")[1].split(" ")[0]
        castleAvail = re.split(" ([KQkq-]{1,4}) ", notation)[1]
        enPassant = re.split(" ([a-zA-Z1-8-]{1,2}) ", notation)[3]
        halfmove = re.split(" \D*", notation)[1]
        fullmove = re.split(" \D*", notation)[2]
        
        for i in temp:
            if i.__contains__(" "):
                ranks.append(i.split(" ")[0])
                break
            ranks.append(i)
            
        print(*ranks)
        print(player)
        print(castleAvail)
        print(enPassant)
        print(halfmove)
        print(fullmove)
        
        board = ""
        
        for i in ranks:
            if i == "8":
                board += "........\n"
                continue
            for k in [char for char in i]:
                # print(k)
                if k.isdigit():
                    for j in range(int(k)):
                        board += "."
                    continue
                board += k
            board += "\n"
        
        print(*board)
    
    def PrintBoard(self, BoardNot):
        # KBQRNP
        notation = self.FENtoBoard()
        printboard = []
        
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
                    
                if notation[rank].lower() == "k":
                    tile = self.white_pieces["king"]
                elif notation[rank].lower() == "q":
                    tile = self.white_pieces["queen"]
                elif notation[rank].lower() == "b":
                    tile = self.white_pieces["bishop"]
                elif notation[rank].lower() == "n":
                    tile = self.white_pieces["knight"]
                elif notation[rank].lower() == "r":
                    tile = self.white_pieces["rook"]
                elif notation[rank].lower() == "p":
                    tile = self.white_pieces["pawn"]
                    
                if isLightSquare:
                    printboard.append(Back.GREEN + color + " " + tile + " ")
                else:
                    printboard.append(Back.BLUE + color + " " + tile + " ")
            

if __name__ == "__main__":
    l = logic()
    l.PrintBoard
    #l.FENtoBoard("rnbqkbnr/pppppppp/6pp/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e3 0 1")
