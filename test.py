import random
secretnumber=random.randint(1,50)
attempt=0
maxattempt=5
won=False
print("welcome to the number guessing game")
print("guess the secret number between 1 and 50")
print("you have 5 attempts")
while attempt < maxattempt and not won: 
    guess=int(input("enter your guess: "))
    attempt = attempt+1
    if guess==secretnumber: 
        print("yaya you got the number")
        won=True
    else: 
        difference=abs(secretnumber-guess)
        if difference > 20: 
            print("ice cold")
        elif difference > 10: 
            print("cold")
        elif difference > 5: 
            print("warm")
        else: 
            print("hot")

