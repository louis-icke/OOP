import random

class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.current_face = 0

    def showFace(self):
        print(self.current_face)

    def roll(self):
        self.current_face = random.randint(1,self.sides)
        self.showFace()


six = Dice(6)
six.roll()
