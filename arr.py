import array
numbers = array.array("i",  [1, 3, 5, 3, 7, 9, 3])
print(numbers)
print(numbers.count(3))
numbers.reverse()
print(numbers)