from abc import ABC, abstractmethod

class Dog(ABC):
    @abstractmethod
    def eat(self):
        pass
    
class Bobo(Dog):
    def eat(self):
        print('eating.')

tom = Bobo()
tom.eat()
