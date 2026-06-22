import random
computernumber = random.randint(1,6)
num = int(input("enter a number between 1 and 6: "))
if computernumber == num: 
    print("congrats u win!!!")
else: 
    print("please try again:(")
print("computer chose ", computernumber)