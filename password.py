import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

password = list("Aa1Bc2Xy")

random.shuffle(password)

print("Generated Password:", "".join(password))