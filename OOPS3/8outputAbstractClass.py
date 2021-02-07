from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        print('function of class A called')

    @abstractmethod
    def fun2(self):
        pass

class B(A):
    def fun1(self):
        print('function 1 called')
    def fun2(self):
        print('function 2 called')
o = B()
o.fun1()