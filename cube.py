def cube(number): 
    return number * number * number
def checkno(number):
    if number%3 == 0: 
        result=cube(number)
        print(result)
    else: 
        print("number is not divisible by 3")
checkno(3)