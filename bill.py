unit=int(input("enter your electricity consume: "))
if unit < 50: 
    cost = unit*2.60
    total=cost+25
elif unit < 100: 
    cost= unit*3.25
    total=cost+35
elif unit <200: 
    cost=unit*5.26
    total=cost+45
else: 
    cost=unit*8.45
    total=cost+75
print("total bill=",total)
