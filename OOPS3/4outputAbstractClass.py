from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

class B(A):

    def fun1(self):
        print('function 1 called')
o = B()
o.fun1()