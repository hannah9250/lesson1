from abc import ABC, abstractmethod
class Animal: 
    @abstractmethod
    def move(self): 
        pass
class Human(Animal): 
    def move(self): 
        print("human moves with 2 legs")
class Dog(Animal): 
    def move(self): 
        print("dog moves with 4 legs")
i = Human()
d = Dog()
i.move()
d.move()