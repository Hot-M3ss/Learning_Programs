"""A text adventure meant to expand my skills"""


def main():
    """Main Functiom"""
    inventory = []

    while True:
        introduction()


def introduction():
    player_action(['n'], ['torch'])


def room_one():
    ...


def room_two():
    ...


def player_action(directions, objects):
    """Prompts player for a command."""
    valid_commands = {
        'travel': ['go', 'head', 'travel', 'walk'],
        'collect_item': ['take', 'collect', 'grab'],
        'inventory_action': ['open'],
        'use_item': ['light', 'burn', 'cut']
    }

    while True:
        raw_input = input("\n> ").lower().strip()

        if raw_input == 'help':
            for key, command in valid_commands.items():
                print(f"{key}: {command}")
            continue

        try:
            (verb, noun) = raw_input.split(" ")
        except ValueError:
            print("I don't understand.")
            continue

        if verb in valid_commands['travel']:
            if noun[0] in directions:
                return noun[0]
            else:
                print(f"you can't go: {noun}")
                continue

        elif verb in valid_commands['collect_item']:
            if noun in objects:
                return noun
            else:
                print(f"Could not find {noun} in room")
                continue

        else:
            print("Command not recognized, use help for valid commands")


def add_to_inv(object):
    ...


def inventory(objects):
    ...


main()
