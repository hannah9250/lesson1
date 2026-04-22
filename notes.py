amount= int(input("write the amount: "))
note100=amount//100
amount=amount%100
note50=amount//50
amount=amount%50
note10=amount//10
amount=amount%10
print("note100: ",note100)
print("note50: ", note50)
print("note10: ",note10)
