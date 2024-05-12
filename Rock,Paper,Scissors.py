import random

choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock,paper or scissors: ").lower()
if computer == player:
    print("computer: "+computer)
    print("player: " + player)
    print("tie")
elif player == "rock":
    if computer == "paper":
        print("computer: " + computer)
        print("player: " + player)
        print("you have lost:(")
elif player == "paper":
    if computer == "rock":
        print("computer: " + computer)
        print("player: " + player)
        print("you have won:)")
    if computer == "scissors":
        print("computer: " + computer)
        print("player: " + player)
        print("you have lost:(")
elif player == "paper":
    if computer == "scissors":
        print("computer: " + computer)
        print("player: " + player)
        print("you have lost:(")
    if computer == "rock":
        print("computer: " + computer)
        print("player: " + player)
        print("you have won:)")