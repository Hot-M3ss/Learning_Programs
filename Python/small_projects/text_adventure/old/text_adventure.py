"""
Welcome to the TEXT ADVENTURE!!! This may be an ambitious goal, 
but I would like to implement a basic story with an inventory and
possible combat. At this moment I want to leave combat out and focus on story.
"""
from os import name as os_name
from os import system as os_system


def main() -> None:
    """This controls the main logic of the Text Adventure"""
    clear_terminal()
    introduction()
    room_one(first_entry = True)


def introduction() -> None:
    """Prompts user for their name and introduces the game."""
    candidate_name = input("\nEnter your name: ").title().strip()
    print(candidate_name)

    print(f"""Welcome candidate to the selection for the Elemental of Fire.
It's a pleasure to finally be able to speak with you {candidate_name}.
You may be asking yourself who I am, and to that I can only say one thing.""")


def player_action(directions, objects):
    """Prompts the player for commands and checks if they are valid.
    Go: The player can choose which direction to go.
    Take: allows the player to pickup specific items."""
    while True:
        c = input("").strip()

        try:
            (verb, noun) = c.lower().split(" ")

        except ValueError:
            print("\nI don't understand.")
            continue

        if verb == "go":
            if noun[0] in directions:
                return verb, noun[0]
            else:
                print(f"you can't go {noun}.")
        elif verb == "take":
            if noun[0] in objects:
                break
            else:
                print(f"There is no {noun} to take.")
        else:
            print("I only understand the commands: go, take")

def room_one(first_entry: bool = False):
    """Displays the first room, not much for the player to do besides push forward."""
    if first_entry:
        print("First Room: first entry text")
    else:
        print("First Room: revisit text")

    (verb, noun) = player_action(['n'], [])

    if verb == "go":
        if noun[0] == 'n':
            room_two()


def room_two(first_entry: bool = False):
    """Displays the first room, not much for the player to do besides push forward."""
    if first_entry:
        print("Second room: first entry text")
    else:
        print("Second Room:A secondary room")


def clear_terminal():
    """Clears the terminal depending on the OS"""
    if os_name == "posix":
        os_system("clear")
    elif os_name == "nt":
        os_system("cls")


main()
