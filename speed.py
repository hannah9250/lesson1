a=int(input("speed 1: "))
b=int(input("speed 2: "))
c=int(input("speed 3: "))
avg=(a+b+c)/3
print(avg)
if a < avg: 
    print("cyclist 1 is slower than average")
elif b < avg: 
    print("cyclist 2 is slower than average")
else: 
    print("cyclist 3 is slower than average")
