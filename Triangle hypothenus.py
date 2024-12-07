import math



class Triangle:
    ''' DOCTSTRING BABYYYYYYYYYYY'''
    def __init__(self,side1,side2,side3,Boobs):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    
    def ptheorem(self):
        self.hypothenus = math.sqrt(self.side1**2 + self.side2**2)
        return self.hypothenus
    
    
class Boobs:
    def __init__(self,Triangle):
        self.boob = Triangle.side1
        
        
if __name__ == "__main__":
    checktriangle = Triangle(6,7,5)
    print(checktriangle.ptheorem())
    boobs = Boobs(checktriangle)
    print(boobs.boob)
    
