class Vector:
    def __init__(self,x,y):
        self.x= x 
        self.y = y
    def __add__(self,vector):
        return Vector (self.x+vector.x, self.y+vector.y)
    def __sub__(self,vector):
        return Vector(self.x-vector.x, self.y-vector.y)

v1 = Vector(3,4)
v2 = Vector(5,6)
v3 = v1+v2
print(f"{v3.x},{v3.y}")