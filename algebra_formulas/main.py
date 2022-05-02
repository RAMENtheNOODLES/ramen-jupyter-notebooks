import math
from fractions import Fraction

class AlgebraFormulas:
    def __init__(self):
        pass
    
    @staticmethod
    def Quadratic(a, b, c, solve=False):
        x = [0, 0]
        
        x[0] = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x[1] = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        
        if not solve:
            return x
        
    
    @staticmethod
    def DTF(decimal):
        return Fraction(decimal)
    

if __name__ == "__main__":
    AF = AlgebraFormulas
    print(AF.Quadratic(1, 6, -27))
    
    print(AF.DTF(1))
