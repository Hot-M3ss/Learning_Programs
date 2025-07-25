"""test"""

import os
import json
import time
import remove_file


def generate_blank_json():
    """test"""
    # desktop = os.path.join(os.path.expanduser("~"), "Documents")
    # file_path = os.path.join("~Python/small_projects/text_adventure","test.json")
    file_path = os.path.join("Python/small_projects/text_adventure", "rooms.json")

    rooms = []
    player_state = {
        "in_room":None,
        "inventory":[],
        "flags":{
            "seen_intro":False
        }
    }

    # items = {"name":"Torch","Unlit":True}

    for i in range(21):
        rooms.append({"id":i+1, "room_intro":"", "room_revisit":"", "objects":[], "connections":{"north": None,"south": None,"east": None,"west": None}})

    data = {"player_state": player_state, "rooms":rooms}

    with open(file_path, 'x+', encoding="UTF-8") as file:
        json.dump(data,file,indent=4)


remove_file.remove_file()
time.sleep(2)
generate_blank_json()
