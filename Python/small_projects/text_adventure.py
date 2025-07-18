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

def introduction() -> None:
    """Prompts user for their name and introduces the game."""
    candidate_name = input("\nEnter your name: ").title().strip()
    print(candidate_name)

    print(f"""Welcome candidate to the selection for the Elemental of Fire.
It's a pleasure to finally be able to speak with you {candidate_name}.
You may be asking yourself who I am, and to that I can only say one thing.""")


def clear_terminal():
    """Clears the terminal depending on the OS"""
    if os_name == "posix":
        os_system("clear")
    elif os_name == "nt":
        os_system("cls")


main()
