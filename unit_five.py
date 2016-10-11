# James Bankole Unit Five 10/11/16
# This program asks the user if they want to play a guessing game. If yes, prompts them to guess numbers between 1 and
# 100 until they are correct and displays how many times they guessed. If no, thanks the user and ends the program.


import random


def intro():
    """This function asks the user if they would like to play and if yes, continues with the program. If no, thanks
    the user and ends the program"""
    while True:
        userPlay = input("Would you like to play my guessing game? (y or n)")
        if userPlay == "y":
            return True
        elif userPlay == "n":
            print("Thanks for playing my game, goodbye!")
            return False


def getRandom():
    """This function gets the random number used in the program"""
    return random.randint(1, 101)


def userGuess():
    """This function prompts the user for their guess and continues program if guess is between 1 and 100"""
    while True:
        guess = int(input("Pick a number between 1 and 100."))
        if guess >= 1 and guess <= 100:
            return guess


def guessRange(randomN):
    """This function tells the user if their guess was too high or too low and then calculates and tells the user the
    amount of times the user guessed."""
    times = 0
    while True:
        userG = userGuess()
        if userG < randomN:
            print("Your guess was too low.")
            times += 1
        elif userG > randomN:
            print("Your guess was too high.")
            times += 1
        else:
            print("Congratulations, you are correct!")
            times += 1
            print("You tried", times, "time(s)")
            break


def main():
    while intro():
        randomN = getRandom()
        guessRange(randomN)


main()
