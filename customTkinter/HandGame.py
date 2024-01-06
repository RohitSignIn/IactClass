# Hand Game Logic => Stone Paper Scissor

# import random
import random

player1Count = 0
player2Count = 0
chances = 3

while(chances):
    # prints a random value from the list
    choices = ["Stone", "Paper", "Scissor"]

    player1 = random.choice(choices)
    player2 = random.choice(choices)

    if(player1 == player2):
        continue
    if(player1 == "Stone" and player2 == "Scissor"):
        player1Count += 1
    if(player1 == "Paper" and player2 == "Stone"):
        player1Count += 1
    if(player1 == "Scissor" and player2 == "Paper"):
        player1Count += 1

    if(player2 == "Stone" and player1 == "Scissor"):
        player2Count += 1
    if(player2 == "Paper" and player1 == "Stone"):
        player2Count += 1
    if(player2 == "Scissor" and player1 == "Paper"):
        player2Count += 1
    
    chances -= 1

if(player1Count > player2Count):
    print("winner is player 1")
else:
    print("winner is player 2")

        



    

