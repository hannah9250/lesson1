class Employee:
    def __init__(self): 
        print("employee joined the company")
    def __del__(self): 
        print("employee left the company")
def company(): 
    c = Employee()
    del c
company()
