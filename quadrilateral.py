import sys

class Quadrilateral:

    def __init__(self, *args):
        # self.side = 0
        # self.length = 0
        # self.breadth = 0

        if len(args) == 1:
            # self.side = args[0]
            self.length = self.breadth = args[0]
        elif len(args) == 2:
            self.length = args[0]
            self.breadth = args[1]

    def printArea(self):
        # if self.side != 0:
        if self.length == self.breadth:
            # print("Area of square: ", self.length * self.side)
            print("Area of square: ", self.length * self.length)
        else:
            print("Area of rectangle: ", self.length * self.breadth)

S1 = Quadrilateral(5,9)
S1.printArea()