from abc import ABC, abstractmethod
class Base(ABC): 
    def display (self): 
        print("this is a value")
    @abstractmethod
    def show(self): 
        pass
class Child(Base): 
    def show(self): 
        print("abstraction is being implemented")
g = Child()
g.display()
g.show()

        
    

