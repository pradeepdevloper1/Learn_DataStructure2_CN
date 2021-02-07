class Mother:
    def print(self):
        print('Print of Mother')

class Father:
    def print(self):
        print('Print of Father')

class Child(Father,Mother):
    def __init__(self,name):
        self.name=name
    def printChild(self):
        print('Name of Child=',self.name)


c=Child("Rohan")
c.printChild()
c.print()                    