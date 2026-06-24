def add(a,b): 
    return a+b
def subtract(a,b): 
    return a - b
def multiply(a,b): 
    return a * b
def divide(a,b): 
    return a / b
try: 
    print("CALCULATOR")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    choice= input("enter you choice (1 - 4): ")
    num1= float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    if choice == "1": 
        print("result = ", add(num1,num2))
    elif choice == "2": 
        print("result = ", subtract(num1,num2))
    elif choice == "3": 
        print("result = ", multiply(num1,num2))
    elif choice =="4": 
        print("result = ", divide(num1,num2))
    else: 
        print("invalid choice")
except ZeroDivisionError: 
    print("you can not divide by zero")
except ValueError: 
    print("please enter a number")
    




