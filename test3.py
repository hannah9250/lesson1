students = {
    "hannah" : 98, 
    "liam" : 82, 
    "olivia" : 78, 
    "bob" : 56, 
    "emma" : 92,
}
total = 0
for score in students.values(): 
    total += score
average = total/len(students)
print("average: ", average)
topper = max(students, key = students.get)
print("topper: ", topper)
loser = min(students, key = students.get)
print("loser: ", loser)
name = input("please enter students name: ")
grade = students.get(name)
if grade is not None: 
    print(name,":", grade)
else: 
    print("student not found in grade book")
