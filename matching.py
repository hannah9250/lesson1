word= ["abc", "aba", "1221", "xy", "aa"]
count = 0
for i in word:
    if len(i) >= 2 and i[0] == i[-1]:
        count = count + 1
print(count)
