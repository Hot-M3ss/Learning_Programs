# def testOne():
#     while(True):
#         test = input("Number: ").replace(",","")
#         number = verifyNumber(test)
#         print(f"{type(number)} success: {number}")

# def verifyNumber(number):
#     try:
#         return int(number)
#     except ValueError:
#         print(f"Int Fail: {number}")

#     try:
#         return float(number)
#     except:
#         print(f"Float Fail: {number}")

# testOne()

# def testTwo():
#     while(True):
#         raw = input("Number: ")
#         cleaned = raw.replace(",","")
#         number = verifyNumber(cleaned)
#         print(f"{type(number)} success: {number}")

# def verifyNumber(number):
#     try:
#         return int(number)
#     except ValueError:
#         pass

#     try:
#         return float(number)
#     except ValueError:
#         return None

# testTwo()

# def viewList(loadedList, includeUpdateList: bool):
#     print("Welcome to your todo list!\n")
#     if loadedList != []:
#         maxValueLength = max(len(x['task']) for x in loadedList)
#         for id, item in enumerate(loadedList, start=1):
#             status = f'Due by {item["date"]:<10}' if item["done"] == False else "Completed"
#             print(f'{id:>3}. Task: {item["task"]:<{maxValueLength}} | Status: {status:<17} | Note: {item["note"]:<10}')
#     else:
#         print(f"No items loaded; has a file been generated?")
#     if includeUpdateList == True:
#         maxKeyLength = max(len(x) for x in loadedList[taskNumber])
#         for id, item in enumerate(loadedList[taskNumber], start=1):
#             print(f'{id:>3}. {f'{item}:':<{maxKeyLength+1}} {loadedList[taskNumber][item]}')


# maxTaskLength = max(len(x) for x in newList[taskNumber])
# for id, item in enumerate(newList[taskNumber], start=1):
#     print(f'{id:>3}. {f'{item}:':<{maxTaskLength+1}} {newList[taskNumber][item]}')

# maxTaskLength = max(len(x['task']) for x in loadedList)
# for id, item in enumerate(loadedList, start=1):
#     status = f'Due by {item["date"]:<10}' if item["done"] == False else "Completed"
#     print(f'{id:>3}. Task: {item["task"]:<{maxTaskLength}} | Status: {status:<17} | Note: {item["note"]:<10}')

"""
Welcome to the TEXT ADVENTURE!!! This may be an ambitious goal, 
but I would like to implement a basic story with an inventory and
possible combat.
"""
class Enemy:
    """f"""
    def __init__(self, name: str, health: int, enemy_type: str):
        self.name = name
        self.health = health
        self.enemy_type = enemy_type

    def __repr__(self):
        return f"success: {self.name}"

    def reduce_health(self, damage_amount: int, weak: bool):
        """applies damage to enemies dependant on if the enemy is weak to damage."""
        if weak:
            crit = damage_amount * 2
            self.health = self.health - crit
        else:
            self.health = self.health - damage_amount

def main() -> None:
    """This controls the main logic of the Text Adventure"""
    enemy_one = Enemy("final boss", 5000, "fire")
    damage = int(input("how much damage do you want to do? "))

    enemy_one.reduce_health(damage, True)

    print(enemy_one.health)


# def battle_loop(enemy_name: str) -> None:
#     """This controls the main battle loops, the idea of this module
#     is to initialize a battle sequence, right now there will only
#     be one enemy for learning purposes."""

main()
