english=int(input("enter english marks: "))
python=int(input("enter python marks: "))
physics=int(input("enter physics marks: "))
science=int(input("enter science marks: "))
math=int(input("enter math marks: "))
avg=(english + python + physics + science + math)/5
print(avg)
if avg >= 91: 
    print("grade A1")
elif avg >= 81: 
    print("grade A2")
elif avg >= 71: 
    print("grade B1")
elif avg >= 61: 
    print("grade B2")
elif avg >= 51: 
    print("grade D1")
else: 
    print("FAILED, YOU SHOULD HAVE STUDIED HARDER, FROM HANNAH THE LAZY CODER")



            