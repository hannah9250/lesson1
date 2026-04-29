height=float(input("enter your height in cm: "))
weight=float(input("enter your weight in kg: "))
height=height/100
bmi=weight/(height*height)
print("your bmi is: ",bmi)
if bmi < 18.5: 
    print("under weight")
elif bmi < 25: 
    print("normal weight")
elif bmi < 30: 
    print("over weight")
else: 
    print("obese")
