import json

monsters = dict()

with open('5e-SRD-Monsters.json') as data_file:
    data = json.load(data_file)
    count = len(data)-1

monster_file = open('5e-SRD-Monsters.json')
monster_json_str = monster_file.read()
for i in range(count):
    monster_json_data = json.loads(monster_json_str)[i]
    monsters[monster_json_data['name']] = monster_json_data
print(monsters['Adult Black Dragon']['actions'][0]['name'])


'''
with open('5e-SRD-Monsters.json') as data_file:
    data = json.load(data_file)

for j in range(len(data)-1):
    print(data[j]["name"])
    print(data[j]["size"])
    print(data[j]["subtype"], data[j]["type"])
    print(data[j]["alignment"])
    print(data[j]["armor_class"])
    print(data[j]["speed"])
    print("str", data[j]["strength"])
    print("dex", data[j]["dexterity"])
    print("con", data[j]["constitution"])
    print("int", data[j]["intelligence"])
    print("wis", data[j]["wisdom"])
    print("cha", data[j]["charisma"])


    try:
        print("str save +", data[j]["strength_save"])
    except KeyError:
        pass
    try:
        print("dex save +", data[j]["dexterity_save"])
    except KeyError:
        pass
    try:
        print("con save +", data[j]["constitution_save"])
    except KeyError:
        pass
    try:
        print("wis save +", data[j]["wisdom_save"])
    except KeyError:
        pass
    try:
        print("cha save +", data[j]["charisma_save"])
    except KeyError:
        pass

    print(data[j]["damage_vulnerabilities"])
    print(data[j]["damage_resistances"])
    print(data[j]["damage_immunities"])
    print(data[j]["condition_immunities"])
    print(data[j]["senses"])
    print(data[j]["languages"])

    try:
        len(data[j]["special_abilities"])
        print("\nSpecial Abilities:")
        for i in range(len(data[j]["special_abilities"])):
            print(data[j]["special_abilities"][i]["name"])
            print(data[j]["special_abilities"][i]["desc"])
            print
    except KeyError:
        pass

    
        
    try:
        len(data[j]["actions"])
        print("Actions:")
        for i in range(len(data[j]["actions"])):
            print(data[j]["actions"][i]["name"])
            print(data[j]["actions"][i]["desc"])
            print
    except KeyError:
        pass
    


    try:
        len(data[j]["legendary_actions"])
        print("\nLegendary Actions:")
        for i in range(len(data[j]["legendary_actions"])):
            print(data[j]["legendary_actions"][i]["name"])
            print(data[j]["legendary_actions"][i]["desc"])
            print
    except KeyError:
        pass
'''
