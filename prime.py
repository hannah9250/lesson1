lower=int(input("enter lower range: "))
upper=int(input("enter upper range: "))
for num in range(lower,upper+1): 
    if num > 1: 
        isprime = True
        for i in range(2,num): 
            if num % i == 0: 
                isprime=False
                break
        if isprime: 
            print(num)