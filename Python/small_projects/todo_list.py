import os
import json


def main() -> None:
    desktop = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(desktop, "todolist.json")

    loaded_list = load_existing_list(file_path)
    option_select(file_path, loaded_list)


def load_existing_list(file_path) -> list:
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            loaded_list = json.load(file)
        return loaded_list
    except FileNotFoundError:
        return []


def view_list(loaded_list) -> None:
    print("Welcome to your todo list!\n")
    if loaded_list:
        max_task_length = max(len(x['task']) for x in loaded_list)
        for idx, item in enumerate(loaded_list, start=1):
            status = f'Due by {item["date"]:<10}' if item["done"] is False else "Completed"
            print(f'{idx:>3}. Task: {item["task"]:<{max_task_length}} | Status: {status:<17} | Note: {item["note"]:<10}')
    else:
        print("No items loaded; has a file been generated?")


def option_select(file_path, loaded_list) -> None:
    while True:
        clear_terminal()
        view_list(loaded_list)

        print("\nWhat would you like to do?\n\n1. add a task\n2. update a task\n3. delete a task\n\ns. save and exit\n")
        match input("Option: ").lower():
            case '1':
                loaded_list = add_task(loaded_list)
            case '2':
                loaded_list = update_task(loaded_list)
            case '3':
                loaded_list = delete_task(loaded_list)
            case 's':
                write_to_file(file_path, loaded_list)
                break
            case _:
                print("Not a valid option!")


def add_task(loaded_list: list) -> list:
    clear_terminal()
    view_list(loaded_list)
    while True:
        match input("\nWould you like to add a task? (y/n): ").lower():
            case 'y':
                todo_name = input("\nTask Name: ")
                todo_date = input("Task Due (yyyy-mm-dd): ")
                todo_note = input("Task Note: ")

                loaded_list.append({
                    "task": todo_name, 
                    "date": todo_date, 
                    "note": todo_note, 
                    "done": False})
                
                return loaded_list
            case _:
                return loaded_list


def update_task(loaded_list: list) -> list:
    new_list = copy_list(loaded_list)

    clear_terminal()
    view_list(new_list)
    task_number = int(input("\nWhich task would you like to open?: "))-1

    while True:
        clear_terminal()
        view_list(new_list)
        print("\nPlease choose an option below.\n")
        max_task_length = max(len(x) + 1 for x in new_list[task_number])
        for idx, item in enumerate(new_list[task_number], start=1):
            print(f'{idx:>3}. {item + ":":<{max_task_length}} {new_list[task_number][item]}')

        print(f"\n{'d':>3}. discard changes \n{'s':>3}. save changes")

        match input("\nOption: ").lower():
            case '1':
                new_list[task_number].update({'task': input("\nNew Task Name: ")})

            case '2':
                new_list[task_number].update({'date': input("\nNew due date (yyyy-mm-dd): ")})

            case '3':
                new_list[task_number].update({'note': input("\nNew Task Note: ")})

            case '4':
                inv_value = not new_list[task_number]['done']
                new_list[task_number].update({'done': inv_value})

            case 's':
                return new_list
            
            case 'd':
                return loaded_list
            
            case _:
                print("Not a valid option")


def delete_task(loaded_list) -> list:
    new_list = copy_list(loaded_list)
    while True:
        clear_terminal()
        view_list(new_list)
        print('\n1. delete a task\n\nd. discard changes\ns. save changes')
        match input("\nWould would you like to do?: ").lower():
            case '1':
                try:
                    task_to_delete = int(input("\nWhich task would you like to delete? "))
                    new_list.remove(new_list[task_to_delete-1])
                except ValueError:
                    print("Not a valid number!")
                except IndexError:
                    if len(loaded_list) == 0:
                        print("There are no entries to delete!")
                    else:
                        print(
                            f"You can delete a range of 1-{len(new_list)} entries.")
            case 'd':
                return loaded_list
            case 's':
                return new_list


def clear_terminal() -> None:
    """Clear the terminal screen based on the OS."""
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


def copy_list(loaded_list) -> list:
    new_list = []
    for x in loaded_list:
        new_dict = {}
        for item in x:
            key_value = x[item]
            new_dict.update({item:key_value})
        new_list.append(new_dict)
    return new_list
    # return [dict(item) for item in loaded_list] <- While this is more efficient, I like my old system.


def write_to_file(file_path, loaded_list: list) -> None:
    with open(file_path, 'w',encoding="UTF-8") as file:
        json.dump(loaded_list, file, indent=4)
    print("write successful!")


main()
