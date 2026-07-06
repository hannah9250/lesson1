test =  {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
count = 0
for value in test.values(): 
    if value == 2:
        count = count + 1
print(count)