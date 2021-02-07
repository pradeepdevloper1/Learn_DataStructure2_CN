class Vehicle:
     def __init__(self,color,maxSpeed):
         self.color = color
         self.__maxSpeed=maxSpeed
     def getMaxSpeed(self):
         return self.__maxSpeed
     def print(self):
         print("color= ",self.color)
         print("maxSpeed= ",self.__maxSpeed)

class Car(Vehicle):
    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears = numGears
        self.isConvertible=isConvertible

    def print(self):
        #self.print()   undergo  infinite loop
        super().print()
        print("numGears= ",self.numGears)
        print("isConvertible= ",self.isConvertible)


c = Car('black',105,5,False)
c.print()