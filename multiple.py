try: 
    num1= int(input("enter a number: "))
    print (500/num1)
except ZeroDivisionError: 
    print("you cannot divide by 0")
except ValueError: 
    print("please enter a number")
finally: 
    print("thank you")