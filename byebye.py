valid = False
while not valid: 
    num=int(input("enter a number: "))
    if num%2 == 0: 
        while True: 
            print("BYEBYE")
    else: 
        print("number is not divisible by 2")
        valid= True