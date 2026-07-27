class IOString:
    def __init__(self):
        self.str1 = ""
    def show(self): 
        self.str1 = input("enter a string: ")
    def upper(self): 
        print(self.str1.upper())
s = IOString()
s.show()
s.upper()
