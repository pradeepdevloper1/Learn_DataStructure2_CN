from abc import ABC,abstractmethod

class Automobile(ABC):
    def __init__(self):
        print("Automobile is created")

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

c=Car() 
c.start()               
