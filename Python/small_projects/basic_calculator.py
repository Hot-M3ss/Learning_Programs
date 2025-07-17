from os import name, system

def main():
    while(True):
        print("Welcome to my basic calculator!")
        firstNumber, secondNumber = setNumbers()
        print("")
        operator = selectOperation()
        try:
            result = calculate(firstNumber, operator, secondNumber)
            print(f"{firstNumber} {operator} {secondNumber} = {result}")

        except ZeroDivisionError:
            print("\nCannot divide by zero, enter new numbers or select a different operation.\n")

def clearScreen():
    if name == 'posix':
        system("clear")
    if name == 'nt':
        system("clear")

def setNumbers():
    while(True):
        try:
            firstNumber = validateNumber(input("\nplease enter the first number: "))
            break
        except ValueError:
            print("\nNot a valid number!")

    while(True):
        try:
           secondNumber = validateNumber(input("please enter the second number: "))
           break
        except ValueError:
            print("\nNot a valid number!")

    return firstNumber, secondNumber

def validateNumber(number):
    try:
        return int(number)
    except ValueError:
        pass
    
    try:
        return float(number)
    except ValueError:
        raise ValueError

def selectOperation():
    operations = ["add", "subtract", "multiply", "divide"]
    for id, item in enumerate(operations, start=1):
        print(f'{id}. {item}')

    while (True):
        match input("\nSelect an operation: "):
            case "1":
                return "+"
            case "2":
                return "-"
            case "3":
                return "*"
            case "4":
                return "/"
            case _:
                print("please make a valid selection!")
        
def calculate(firstNumber, operator, secondNumber):
    try:
        return eval(f"{firstNumber}{operator}{secondNumber}")
    except ZeroDivisionError:
        raise ZeroDivisionError
    



main()