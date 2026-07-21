p = input("what are you choosing rock, paper and scissor:").lower()
import random
u = ["rock","paper","scissors"]
i = random.choice(u)
print("computer chose:", i)
if(i == p):
    print("its a tie ")
elif(p == "rock" and i == "scissors"):
    print("you won")
elif(p == "scissors" and i == "paper"):
    print("you won")
elif(p == "paper" and i == "rock"):
    print("you won")
elif(p == "scissors" and i == "rock"):
    print("computer won")
elif(p == "rock" and i == "paper"):
    print("computer won")
elif(p == "paper" and i == "scissors"):
    print("computer won")
else:
    print("Invalid choice! Please enter rock, paper, or scissors.")