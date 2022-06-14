import random
from re import T
print("Welcome to rock paper scissors!")
"choose R for rock"
"choose P for paper"
"choose S for scissors"

game_options = ["R","P","S"]

while True:
    
    CPU = random.choice(game_options)
    player = None
    
    while player not in game_options:
        
        player = input("make your move: ")
        if player not in game_options:
         print("invalid move, try again!")
        else:
            print("player:", player)
            print("CPU:", CPU)
    
    if player == CPU:
        print("Tie!")
        
    elif player == "R" and CPU == "S": 
        print("rock beats scissors")
        print("player wins!")
    elif player == "R" and CPU == "P":
        print("paper beats rock")
        print("CPU wins!")
    elif player == "P" and CPU == "R":
        print("paper beats rock")
        print("player wins!")
    elif player == "P" and CPU == "S":
        print("scissors beats paper")
        print("CPU wins!")
    elif player == "S" and CPU == "R":
        print("rock beats scissors")
        print("CPU wins!")
    elif player == "S" and CPU == "P":
        print("scissors beats paper")
        print("player wins!")
     
    Endgame = input("Would you like to play game? Y/N: ")
    Answer = input()
    
    if Endgame == "N":
        print("Thank you for playing rock paper scissors")
        break
        