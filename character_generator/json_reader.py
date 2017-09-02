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
        class_name = p_class["class_name"]
        classes[class_name] = {} #adds class to dict using name from json

        if "skill_proficiencies" in p_class:
            skill_proficiencies = {}
            skill_proficiencies["count"] = p_class["skill_proficiencies"]["count"]
            skill_proficiencies["skills"] = p_class["skill_proficiencies"]["skills"].split(", ")
            classes[class_name]["skill_proficiencies"] = skill_proficiencies

        subclasses = {}
        for subclass in (p_class["subclasses"]):
            subclasses[subclass["name"]] = subclass["build"].split(", ")
        classes[class_name]["subclasses"] = subclasses

    return classes

def get_backgrounds(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    backgrounds = {}

    for item in data["backgrounds"]:
        background_name = item["name"]
        backgrounds[background_name] = {"skill_proficiencies": item["skill_proficiencies"].split(", ")}

    return backgrounds

# pprint(get_backgrounds("srd_data/phb_data.json"))
# pprint(a["Wizard"]["subclasses"]["Abjuration"])
