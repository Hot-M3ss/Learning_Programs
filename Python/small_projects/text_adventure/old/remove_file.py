import os

def remove_file():
    file_path = os.path.join("Python/small_projects/text_adventure", "rooms.json")

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"The file '{file_path}' has been successfully deleted.")
        except OSError as e:
            print(f"Error deleting the file '{file_path}': {e}")
    else:
        print(f"The file '{file_path}' does not exist.")
