class Demo: 
    def __init__(self):
        self.__privateVar = 150
    def __privMeth(self): 
        print("this is a private variable")
    def hello(self): 
        print(self.__privateVar)
        self.__privMeth()
obj = Demo()
obj.hello()