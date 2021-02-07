from abc import ABC,abstractmethod

class Automobile(ABC):
    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
        print("Automobile is created")

    @abstractmethod
    def get_no_of_wheels(self):
        return self.no_of_wheels
    @abstractmethod
    def start(self):
        print("start of Automobile is Called")

    @abstractmethod
    def stop(self):
        print("stop of Automobile is Called")

class Car(Automobile):

    def start(self):
        super().start()
        print("start of car is Called")
    def stop(self):
        super().stop()
        print("stop of car is Called")
    
    def get_no_of_wheels(self):
        return super().get_no_of_wheels()

class Bus(Automobile):

    def start(self):
        super().start()
        print("start of Bus is Called")
    def stop(self):
        super().stop()
        print("stop of Bus is Called")
    
    def get_no_of_wheels(self):
        return super().get_no_of_wheels()


c=Car(4) 
print(c.get_no_of_wheels())               

b=Bus(8)
print(b.get_no_of_wheels())
