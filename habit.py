
habits = ("Exercise", "Read", "Watch", "Homework", "Sleep")

completion = (5, 7, 4, 7, 6)

print("Weekly Habits:", habits)
print("Completion Record:", completion)

print("Number of habits:", len(habits))

print("First habit:", habits[0])
print("Last habit:", habits[-1])

print("First three habits:", habits[:3])
print("Last two habits:", habits[3:])

try:
    habits[0] = "Yoga"
except TypeError:
    print("Tuples cannot be changed because they are immutable.")