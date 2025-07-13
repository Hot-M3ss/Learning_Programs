import os
import json

# def createFile(filePath):
#     print("Welcome to your todo list!")
#     # desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    
#     with open(filePath, 'a') as f:
#         f.write('test')



# def loadExistingTodoList():
#     print("logic not implemented")



# def removeTodoItem(entryNumber):
#     ...

# def viewTodoItems():
#     ...



def main():
    print("Welcome to your todo list!")
    desktop = os.path.join(os.path.expanduser("~"), "Documents")
    filePath = os.path.join(desktop, "todoList.json")
    addTodoItem(filePath, loadExistingTodoList(filePath))

def loadExistingTodoList(filePath):
    try:
        with open(filePath, 'r') as file:
            loadedList = json.load(file)
        print(loadedList)
        return loadedList
    except FileNotFoundError:
        print("no file found!")
        todoList = []
        return todoList
    
def addTodoItem(filePath, todoList):

    while (True):
        match input("Would you like to add a(nother) task? (y/n): ").lower():
            case 'y':
                todoname = input("Task Name: ")
                todoDate  = input("Task Due Date: ")
                todoNote = input("Task Note: ")

                todoItem = {"task": todoname, "due date": todoDate, "note": todoNote, "completed": False}

                todoList.append(todoItem)

                print(todoList)
            case 'n':
                break
    
    writeToFile(filePath, todoList)

    # with open(filePath,'r') as file:
    #     loaded_list = json.load(file)

    # print(loaded_list)

def writeToFile(filePath, itemToWrite):

    with open(filePath, 'w') as file:
        json.dump(itemToWrite, file, indent=4)
    print("JSON data has been stored in 'todolist.json'")

main()