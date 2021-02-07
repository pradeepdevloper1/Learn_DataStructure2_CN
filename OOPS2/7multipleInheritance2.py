class Mother:
    def __init__(self):
        self.name="Manju"
    def print(self):
        print("print ogf Mother Called ")   

class Father:
    def __init__(self):
        self.name="Ram"
    def print(self):
        print("print ogf Father Called ")    

class Child(Father,Mother):
    def __init__(self):
        super().__init__()
        
    def printChild(self):
        print('Name of Child=',self.name)


c=Child()
c.printChild()                   