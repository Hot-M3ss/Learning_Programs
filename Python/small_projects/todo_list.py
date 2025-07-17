import os
import json


def main() -> None:
    desktop = os.path.join(os.path.expanduser("~"), "Documents")
    filePath = os.path.join(desktop, "todoList.json")
    loadedList = loadExistingTodoList(filePath)
    optionSelect(filePath, loadedList)


def clearTerminal() -> None:
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


def loadExistingTodoList(filePath) -> list:
    try:
        with open(filePath, 'r') as file:
            loadedList = json.load(file)
        return loadedList
    except FileNotFoundError:
        todoList = []
        return todoList


def viewList(loadedList) -> None:
    print("Welcome to your todo list!\n")
    if loadedList != []:
        maxTaskLength = max(len(x['task']) for x in loadedList)
        for idx, item in enumerate(loadedList, start=1):
            status = f'Due by {item["date"]:<10}' if item["done"] is False else "Completed"
            print(f'{idx:>3}. Task: {item["task"]:<{maxTaskLength}} | Status: {status:<17} | Note: {item["note"]:<10}')
    else:
        print("No items loaded; has a file been generated?")


def optionSelect(filePath, loadedList) -> None:
    while True:
        clearTerminal()
        viewList(loadedList)

        print("\nWhat would you like to do?\n\n1. add a task\n2. update a task\n3. delete a task\n\nS. save to file and exit\n")
        match input("Option: ").lower():
            case '1':
                loadedList = addTask(loadedList)
            case '2':
                loadedList = updateTask(loadedList)
            case '3':
                loadedList = deleteTask(loadedList)
            case 's':
                writeToFile(filePath, loadedList)
                break
            case _:
                print("Not a valid option!")


def addTask(loadedList) -> list:
    clearTerminal()
    viewList(loadedList)
    while True:
        match input("\nWould you like to add a task? (y/n): ").lower():
            case 'y':
                todoname = input("\nTask Name: ")
                todoDate = input("Task Due (yyyy-mm-dd): ")
                todoNote = input("Task Note: ")
                loadedList.append({"task": todoname, "date": todoDate, "note": todoNote, "done": False})
                return loadedList
            case _:
                return loadedList


def updateTask(loadedList) -> list:
    newList = copyList(loadedList)
    clearTerminal()
    viewList(newList)
    taskNumber = int(input("\nWhich task would you like to open?: "))-1
    while True:
        clearTerminal()
        viewList(newList)
        print("\nPlease choose an option below.\n")
        maxTaskLength = max(len(x) + 1 for x in newList[taskNumber])
        for idx, item in enumerate(newList[taskNumber], start=1):
            print(f'{idx:>3}. {item + ":":<{maxTaskLength}} {newList[taskNumber][item]}')
        print(f"\n{'d':>3}. discard changes \n{'s':>3}. save changes")

        match input("\nOption: ").lower():
            case '1':
                newList[taskNumber].update(
                    {'task': input("\nNew Task Name: ")})
            case '2':
                newList[taskNumber].update(
                    {'date': input("\nNew due date (yyyy-mm-dd): ")})
            case '3':
                newList[taskNumber].update(
                    {'note': input("\nNew Task Note: ")})
            case '4':
                oppositeValue = (False if newList[taskNumber]['done'] == True else True)
                newList[taskNumber].update({'done': oppositeValue})
            case 's':
                return newList
            case 'd':
                return loadedList
            case _:
                print("Not a valid option")


def deleteTask(loadedList) -> list:
    newList = copyList(loadedList)
    while True:
        clearTerminal()
        viewList(newList)
        print('\n1. delete a task\n\nd. discard changes\ns. save changes')
        match input("\nWould would you like to do?: ").lower():
            case '1':
                try:
                    taskToDelete = int(input("\nWhich task would you like to delete? "))
                    newList.remove(newList[taskToDelete-1])
                except ValueError:
                    print("Not a valid number!")
                except IndexError:
                    if len(loadedList) == 0:
                        print("There are no entries to delete!")
                    else:
                        print(
                            f"You can delete a range of 1-{len(newList)} entries.")
            case 'd':
                return loadedList
            case 's':
                return newList


def copyList(loadedList) -> list:
    newList = []
    for x in loadedList:
        newDict = {}
        for item in x:
            keyValue = x[item]
            newDict.update({item: keyValue})
        newList.append(newDict)
    return newList


def writeToFile(filePath, itemToWrite) -> None:
    with open(filePath, 'w') as file:
        json.dump(itemToWrite, file, indent=4)
    print("write successful!")


main()
