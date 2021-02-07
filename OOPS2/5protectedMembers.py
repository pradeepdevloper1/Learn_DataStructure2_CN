class Vehicle:
     def __init__(self,color,maxSpeed):
         self.color = color
         self._maxSpeed=maxSpeed
     def getMaxSpeed(self):
         return self._maxSpeed
     def print(self):
         print("color= ",self.color)
         print("maxSpeed= ",self._maxSpeed)

class Car(Vehicle):
    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears = numGears
        self.isConvertible=isConvertible

    def print(self):
        #self.print()   undergo  infinite loop
        #super().print()
        print("color= ",self.color)
        print("maxSpeed= ",self._maxSpeed)
        print("numGears= ",self.numGears)
        print("isConvertible= ",self.isConvertible)


c = Car('black',105,5,False)
c.print()

print()


v=Vehicle("RED",18)
v.print()
v._maxSpeed=19
v.print()
