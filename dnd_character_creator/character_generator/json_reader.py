import json
from pprint import pprint

def get_races(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    races = {}

    for race in data["races"]:
        races[race["race_name"]] = {}

        subraces = {}
        for subrace in (race["subraces"]):
            subraces[subrace["name"]] = list(subrace["bonuses"].items())

        races[race["race_name"]]["subraces"] = subraces

    return races

def get_classes(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    classes = {}

    for p_class in data["classes"]:
        classes[p_class["class_name"]] = {} #adds class to dict using name from json

        subclasses = {}
        for subclass in (p_class["subclasses"]):
            subclasses[subclass["name"]] = subclass["build"].split(", ")

        classes[p_class["class_name"]]["subclasses"] = subclasses
    return classes

def get_backgrounds(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    backgrounds = []

    for item in data["backgrounds"]:
        backgrounds.append(item["name"])

    return backgrounds

# pprint(get_races("srd_data/expansion_data.json"))
#pprint(a["Wizard"]["subclasses"]["Abjuration"])
