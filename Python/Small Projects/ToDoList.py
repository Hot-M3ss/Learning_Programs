import os
import json

def main():
    desktop = os.path.join(os.path.expanduser("~"), "Documents")
    filePath = os.path.join(desktop, "todoList.json")
    loadedList = loadExistingTodoList(filePath)
    
    optionSelect(filePath, loadedList)

def clearTerminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def loadExistingTodoList(filePath):
    try:
        with open(filePath, 'r') as file:
            loadedList = json.load(file)
        return loadedList
    except FileNotFoundError:
        todoList = []
        return todoList

def viewList(loadedList):
    print("Welcome to your todo list!\n")

    if loadedList != []:
        maxTaskLength = max(len(x['task']) for x in loadedList)
        for id, item in enumerate(loadedList, start=1):
            status = f'Due by {item["due date"]:<10}' if item["completed"] == False else "Completed"
            print(f'{id:>3}. Task: {item["task"]:<{maxTaskLength}} | Status: {status} | Note: {item["note"]:<10}')
    else:
        print(f"No items loaded; has a file been generated?\n")

def optionSelect(filePath, loadedList):
    while(True):
        clearTerminal()
        viewList(loadedList)

        print("\nWhat would you like to do? (only #4 saves)\n1. add a task\n2. update a task\n3. delete a task\n4. save to file and exit\n")
        match input("Option: ").lower():
            case '1':
                loadedList = addTask(loadedList)
            case '2':
                loadedList = updateTask(loadedList)
            case '3':
                loadedList = deleteTask(loadedList)
            case '4':
                writeToFile(filePath, loadedList)
                break
            case _:
                print("Not a valid option!")
    
def addTask(todoList):
    while (True):
        match input("\nWould you like to add a task? (y/n): ").lower():
            case 'y':
                todoname = input("\nTask Name: ")
                todoDate  = input("Task Due Date (yyyy-mm-dd): ")
                todoNote = input("Task Note: ")
                todoList.append({"task": todoname, "due date": todoDate, "note": todoNote, "completed": False})
                return todoList
            case _:
                return todoList

def updateTask(todoList):
    return todoList

def deleteTask(todoList):
    return todoList

def writeToFile(filePath, itemToWrite):
    with open(filePath, 'w') as file:
        json.dump(itemToWrite, file, indent=4)
    print("write successful!")

main()