
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def display(self):
        print(self.__name + "'s age is: " + str(self.age))

person1 = Person('Adam', 19)
person1.display()

person2 = Person('John',  28)
person2.display()