from random import randint;
from random import choice;
import os;

def intro():
    clearTerminal()
    print("Welcome to the Number Guessing Game!\n")
    compareGuess(generateNumber(), PlayerGuess())

def clearTerminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def generateNumber():
    while (True):
        match input("Set the range? (y/n): ").lower():
            case "y":
                rangeStart, rangeEnd = setRange()
                break
            case "n":
                rangeStart = 1
                rangeEnd = choice(range(10,100,5))
                break
            case _:
                print("Please enter y or n!")
    clearTerminal()
    print(f"The range set is between {rangeStart}-{rangeEnd}\n")
    return randint(rangeStart, rangeEnd)

def setRange():
    clearTerminal()
    while(True):
        try:
            print("Please enter your range below. Don't make it too easy!\n")
            rangeStart = int(input("Start: "))
            rangeEnd = int(input("End: "))
            if rangeStart > rangeEnd:
                raise ArithmeticError
            return rangeStart, rangeEnd
        except ValueError:
            print("Not a valid number!")
        except ArithmeticError:
            print("Range start must be less than range end!")

def PlayerGuess():
    while(True):
        try:
            return int(input(f"Please enter your guess: "))
        except ValueError:
            print("Not a valid number!\n")
    
def compareGuess(computersNumber, playerGuess):
    if computersNumber == playerGuess:
        print("You Won!")
    else:
        print("Better luck next time!")

intro()