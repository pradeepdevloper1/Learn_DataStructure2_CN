from abc import ABC,abstractmethod

class Automobile(ABC):
    def __init__(self):
        print("Automobile is created")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Automobile):
    # def __init__(self,name):
    #     self.name=name
    #     print("car is created =",self.name)
    def start(self):
        pass
    def stop(self):
        pass

c=Car()                
