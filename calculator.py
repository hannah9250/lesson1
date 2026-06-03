def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b): 
    return a/b
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. divide")
choice=int(input("enter you choice: "))
num1 = float(input("enter first number: "))
num2 = float(input("enter seccond number: "))
if choice==1: 
    print(add(num1,num2))
elif choice == 2: 
    print(subtract(num1,num2))
elif choice == 3: 
    print(multiply(num1, num2))
elif choice == 4: 
    print(divide(num1,num2))
else: 
    print("invalid input")