marks = [85, 92, 78, 90, 88]
print("Student Marks:", marks)

print("Number of Students:", len(marks))

print("First Student's Mark:", marks[0])
print("Last Student's Mark:", marks[-1])

print("First Three Marks:", marks[:3])
print("Last Two Marks:", marks[-2:])

print("Marks:")
for mark in marks:
    print(mark)

total = sum(marks)
average = total / len(marks)
smallest = min(marks)
largest = max(marks)

print("MARKS SUMMARY")
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Smallest Mark:", smallest)
print("Largest Mark:", largest)