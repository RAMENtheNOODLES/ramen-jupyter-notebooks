import math
from fractions import Fraction

class AlgebraFormulas:
    def __init__(self):
        pass
    
    @staticmethod
    def Quadratic(a, b, c, solve=False):
        AF = AlgebraFormulas
        x = [0, 0]
        
        x[0] = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x[1] = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        
        if not solve:
            return x
        
        paren1 = f"({AF.DTF(x[0])})"
        
    
    @staticmethod
    def DTF(decimal, returnFraction=False):
        if returnFraction:
            f = Fraction(decimal)
            return f if (f * (1/(decimal)) == 1) else f"{f}/1"
        return Fraction(decimal)
    

if __name__ == "__main__":
    AF = AlgebraFormulas
    print(AF.Quadratic(1, 6, -27))
    print(1/(1/2))
    print(AF.DTF(1, True))
