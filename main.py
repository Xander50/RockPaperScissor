import random
rounds=int(input("How many rounds?:"))
moves=["rock","paper","scissors"]
playerPoints=0
botPoints=0

for i in range(rounds):

    userInput=input("Enter rock, paper, or scissors: ")
    bot=random.choice(moves)

    if userInput == bot:
        print(f"Both chose {userInput}. It's a tie.")
        round+=1
    elif (userInput == "rock" and bot == "scissors") or \
         (userInput == "paper" and bot == "rock") or \
         (userInput == "scissors" and bot == "paper"):
        print(f"Player wins this round! Player chose {userInput} and Bot chose {bot}.")
        playerPoints += 1
    else:
        print(f"Bot wins this round! Player chose {userInput} and Bot chose {bot}.")
        botPoints += 1

if playerPoints > botPoints:
    print("the winner is the Player")
else:
    print("the winner is the Bot")