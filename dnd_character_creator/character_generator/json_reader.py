import json
from pprint import pprint

def get_races(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    races = {}

    for item in data["races"]:
        race = item
        races[race["race"]] = []
        for subrace in (race["subraces"]):
            races[race["race"]].append([subrace["name"], list(subrace["bonuses"].items())])

    return races

def get_classes(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    classes = {}

    for item in data["classes"]:
        p_class = item
        classes[p_class["class"]] = []
        for subclass in (p_class["subclasses"]):
            classes[p_class["class"]].append([subclass["name"], subclass["build"].split(", ")])

    return classes

def get_backgrounds(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    backgrounds = []

    for item in data["backgrounds"]:
        backgrounds.append(item["name"])

    return backgrounds


#pprint(get_races("phb_data.json"))
