class oop():
    name  = ""
    age = ""
    def __init__(self, name, age):
        self.myName = name
        self.myAge = age

    def printObject(self):
        print("what\n")
        print(self.myName," I am ", self.myAge)