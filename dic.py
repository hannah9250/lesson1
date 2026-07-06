students = {

1: {"id": 101, "name": "Rahul", "class": 9, "subject": "Math"},

2: {"id": 102, "name": "Priya", "class": 9, "subject": "Science"},

3: {"id": 101, "name": "Rahul", "class": 9, "subject": "Math"},

4: {"id": 103, "name": "Aman", "class": 9, "subject": "English"}

}
unique_students = {}
seen = []
for key, value in students.items(): 
    if value not in seen: 
        seen.append(value)
        unique_students[key] = value
for key, value in unique_students.items(): 
    print(key, value)
        
    