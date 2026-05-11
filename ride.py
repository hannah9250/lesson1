print("select your ride")
print("1. bike")
print("2. car")
choice= int(input("enter your choice: "))
if choice == 1: 
    print("you selected bike!!!")
    print("1. sports bike")
    print("2. scooter")
    bike=int(input("choose your bike type: "))
    if bike == 1: 
        print("you selected sports bike")
    else: 
        print("you selected scooter")
elif choice == 2: 
    print("you selected car!!!")
    print("1. suv")
    print("2. sedan")
    bike=int(input("choose your car type: "))
    if bike == 1: 
        print("you selected suv")
    else: 
        print("you selected sedan")

    