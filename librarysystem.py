class Library: 
    def __init__(self, book, name):
        self.book = book
        self.name = name
        self.borrowed = False
    def borrow(self): 
        if self.borrowed: 
            print(self.book, "Is already Borrowed")
        else: 
            self.borrowed = True
            print(self.book, "Has Been Borrowed Successfully")
    def returnbook(self):
        if self.borrowed: 
            self.borrowed = False
            print(self.book, "Has been Returned Successfully")
        else: 
            print(self.book, "Was not Borrowed")

b1 = Library("Harry Potter", "J.K Rowling")
b2 = Library("Percy Jackson", "Hannah Naveen")
b3 = Library("Geronimo Stilton", "Geronimo Stilton")
b1.borrow()
b2.borrow()
b2.borrow()
b1.returnbook()
b2.returnbook()
b3.returnbook()





