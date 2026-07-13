from array import array

# Step 1: Create two snack boxes using sets
snack_box1 = {"chips", "apple", "cookies"}
snack_box2 = {"cookies", "banana", "chips"}

snack_box1.add("juice")

shared_snacks = snack_box1.intersection(snack_box2)
print("Shared snacks:", shared_snacks)

snack_counts = array('i', [5, 8, 3])

snack_counts.append(6)
snack_counts.append(8)

print("Number of 8s:", snack_counts.count(8))

snack_counts.reverse()
print("Reversed snack counts:", snack_counts)