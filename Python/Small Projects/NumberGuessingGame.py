import random;
import os;

def intro():
    computersNumber = generateNumber()
    playerGuess = checkPlayerGuess()
    clearTerminal()
    checkGuess(playerGuess, computersNumber)

def setRange():
    while(True):
        try:
            rangeStart = int(input("Please input the start of the range: "))
            rangeEnd = int(input("Please input the end of the range"))
            if rangeStart > rangeEnd:
                raise ArithmeticError
            break
        except ValueError:
            print("Not a valid number!")
        except ArithmeticError:
            print("Range start must be less than range end!")

def checkPlayerGuess():
    while(True):
        try:
            playerGuess = int(input("Please guess a number from 1-100: "))
            break
        except ValueError:
            print("Not a valid number!")

    return playerGuess

def clearTerminal():
    if os.name == "nt":
        os.system("clear")
    elif os.name == "posix":
        os.system("cls")

def checkGuess(playerGuess, computersNumber):
    if playerGuess == computersNumber:
        print("You Won!\n")
    else:
        print("You did not guess correctly!\n")
        
def generateNumber():
    number = random.randint(1, 100)
    return number

intro()