import random
from os import system

def NumberGuessingGame(genNumber):
    system("cls")
    tries = 0
    guess = ""
    while(guess != 0):
        tries += 1
        guess = int(input("Enter your guess: "))
        if(guess == 0):
            break
        if(guess > 100):
            print("The number should be less than 100")
            continue
        elif(guess < 0):
            print("The number should be greater than 0")
            continue
        if(guess == genNumber):
            print("Congratulations! You've guessed the number in", tries, "tries!")
            break
        elif(guess > genNumber):
            print("You need to guess lower")
        elif(guess < genNumber):
            print("You need to guess higher")
        else:
            print("Please enter a valid number")
    return

#generate a random number between 1 and 100

print("""
            Welcome to the Number Guessing Game
            The rules are simple: just guess the number
            Enter 0 to exit the game
""")

play = True
while(play):
    numberRange = "0"
    #ask the user for what range they would like to guess in
    while(not numberRange.isnumeric() or int(numberRange) <= 1):
        numberRange = input("Enter your range: ")
        if(int(numberRange) <= 1):
            print("please enter a number that is neither less than or equal to 1")
        elif(not numberRange.isnumeric()):
            print("please enter a number")

    print(numberRange)
    genNumber = random.randint(1, int(numberRange))
    NumberGuessingGame(genNumber)
    keepPlaying = input("Would you like to play again (y or n)? ")
    play = True if (keepPlaying == "y" or keepPlaying == "yes") else False




