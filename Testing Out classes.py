son = "Mikey"
daughter = "Jessie"

class Mommy:
    def __init__(self,son):
        self.son = "Michael"
        # self.son(run) = "RUN FORREST RUN"
        self.run = "go"
    def son(self):
        self.jump = "Jump"

if __name__ == "__main__":
    SayMOMMY = Mommy(son)
    print(SayMOMMY.son)
    print(SayMOMMY.run)
    # print(SayMOMMY.son(run))
    print(SayMOMMY.son.jump)
    
    print("cow")
    
    
