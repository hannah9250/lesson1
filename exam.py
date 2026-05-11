medical = input("do you have a medical cause?(y/n): ")
if medical == "y": 
    print("you are allowed to take the exam")
else:
    attendence=float(input("enter you attendence percentage: "))
    if attendence >= 75: 
        print("you are allowed to take the exam")
    else: 
        print("you are not allowed to take the exam")

    





