import re

class logic:
    def __init__(self):
        self.starting_pos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    
    def FENtoBoard(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        notation = self.starting_pos
        temp = notation.split("/")
        ranks = []
        player = notation.split(" ")[1].split(" ")[0]
        castleAvail = re.match(" (\w*) ", notation)
        
        for i in temp:
            if i.__contains__(" "):
                ranks.append(i.split(" ")[0])
                break
            ranks.append(i)
            
            

if __name__ == "__main__":
    l = logic()
    
    l.FENtoBoard()
