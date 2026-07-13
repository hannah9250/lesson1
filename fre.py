test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}
print("Test Dictionary:", test_dict)
word = input("Enter the word to check its frequency: ")
print("Frequency:", test_dict.get(word, 0))