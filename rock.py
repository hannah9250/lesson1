import random
choices=["rock", "paper", "scissors"]
computer=random.choice(choices)
user=input("rock, paper or scissors: ")
print("computer: ", computer)
print("user: ", user)
if computer == user: 
    print("match draw")
elif (user == "rock" and computer =="scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"): 
    print("you win")
else: 
    print("computer wins")


