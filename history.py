import json
import os

FILE_NAME = "history.json"


def save_history(city):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            history = json.load(file)
    else:
        history = []

    history.append(city)

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def show_history():
    if not os.path.exists(FILE_NAME):
        print("No search history found.")
        return

    with open(FILE_NAME, "r") as file:
        history = json.load(file)

    if len(history) == 0:
        print("No search history.")
    else:
        print("\nSearch History")
        print("----------------")
        for i, city in enumerate(history, start=1):
            print(f"{i}. {city}")