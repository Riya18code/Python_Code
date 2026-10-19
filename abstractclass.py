from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        print("dog barks") 
d=dog()
d.sound()              