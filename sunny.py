weather = (1, 0, 0, 0, 1, 1, 0)
rainy = 0
sunny = 0
for day in weather: 
    if day == 1: 
        rainy += 1
    else: 
        sunny += 1
print(rainy)
print(sunny)
if rainy > sunny: 
    print("its raining")
else: 
    print("it is sunny :(")
 