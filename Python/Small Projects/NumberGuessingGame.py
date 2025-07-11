import random;
import os;
import platform;

def intro():
    computersNumber = generateNumber()
    playerGuess = checkPlayerGuess()
    clearTerminal()
    checkGuess(playerGuess, computersNumber)

def checkPlayerGuess():
    while(True):
        try:
            playerGuess = int(input("Please guess a number from 1-100: "))
            break
        except ValueError:
            print("Not a valid number!")

    return playerGuess

def clearTerminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def checkGuess(playerGuess, computersNumber):
    if playerGuess == computersNumber:
        print("You Won!\n")
    else:
        print("You did not guess correctly!\n")
        
def generateNumber():
    number = random.randint(1, 100)
    return number

intro()