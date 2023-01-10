#23/01/04 magic method practice 
#SJ

import math

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printVec(self):
        print(f"vector : [{self.x}, {self.y}]")
    def __add__(self, vector):#this is one of the "Magic method"
        self.x = self.x + vector.x
        self.y = self.y + vector.y
        return self
    def __subtract__(self, vector):
        self.x = self.x - vector.x
        self.y = self.y - vector.y
    def norm(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
 
## main
vec1 = Vector(1, 2)
vec2 = Vector(-1, 5)
 
someNorm = vec1.norm()
print(someNorm)
 
#vec1.add(vec2)
(vec1 + vec2).printVec()# this is possible  (adding two classes) because I made a def in class with _add_ in it