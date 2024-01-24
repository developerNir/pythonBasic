# class Parson:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __del__(self):
#         print("Object is being Deconstructed!")
# p = Parson("nirapdak",23)

# how to add to number and 1 dimansonal array of object ---------------
# add x + other X and y + other y --------------------------------------
class Vector:
    #constructor function ------------------
    def __init__(self, x, y,c):
        self.x = x
        self.y = y
        self.c = c
# add And Aplay function ------------
    def __add__(self, other):
        return Vector(self.x + other.x, self.y+other.y, self.c - other.c)
# this is Represasented function
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    # this is Call function ---------------------------
    def __call__(self, *args, **kwargs):
        print("what is Call function")
    def __len__(self):
        return 30



v1 = Vector(34,56, 200)
v2 = Vector(34,30,400)
v3 = v1+v2

print(v3)
print(v3.x)
print(v3.y)
print(v3.c)
v3()# tarminal Printed String Whate is call function
print(len(v2))




