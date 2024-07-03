import math
class Point:
    def _init_(self, x=0, y=0):
        
        self.x = x
        self.y = y

    def distance_to(self, p=None):
        if p is None:
            p=point(0,0)
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)


point1 = Point(4, 4)
point2 = Point(6, 8)
distance = point1.distance_to(point2)
print(f"The distance between the point is {distance}")