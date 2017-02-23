import sys
import os
import random

def makeChoice():
    choices = ["rock", "paper", "scissors"]
    userChoice = input("Rock, Paper, or Scissors? ")
    userChoice = userChoice.lower()
    userChoice = userChoice.strip()
    if userChoice not in choices:
        print("{} is not a valid choice. ".format(userChoice))
        return 0
    else:
        return userChoice

def battle(validChoice):
    computerChoice = random.randint(1,3)
    if computerChoice == 1:
        if validChoice == "rock":
            print("Try Again!")
            return 0
        elif validChoice == "scissors":
            print("You Lose!")
            return validChoice
        else:
            print("You Win!")
            return validChoice
    if computerChoice == 2:
        if validChoice == "paper":
            print("Try Again! ")
            return 0
        elif validChoice == "rock":
            print("You Lose!")
            return validChoice
        else:
            print("You Win!")
            return validChoice
    if computerChoice == 3:
        if validChoice == "scissors":
            print("Try Again! ")
            return 0
        elif validChoice == "paper":
            print("You Lose!")
            return validChoice
        else:
            print("You Win!")
            return validChoice

def main(argv):
    validChoice = 0
    while(validChoice == 0):
        validChoice = makeChoice()
        if validChoice != 0:
            validChoice = battle(validChoice)




if __name__ == "__main__":
    main(sys.argv[1:])
