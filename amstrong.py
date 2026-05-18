num=int(input("enter the number: "))
temp=num
sum=0
while num>0: 
    digit=num%10
    sum=sum+(digit*digit*digit)
    num=num//10
if temp==sum: 
    print("it is an amstrong number")
else: 
    print("it is not an amstrong number")