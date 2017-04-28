from random import *
import json
from heapq import *
__author__ = 'Anton Briganti'


# Utilities: General multi-use functions, not specific to any functionality
def print_list(lst):
    ind = 0
    for _ in lst:
        print(ind, lst[ind])
        ind += 1


def insertion_sort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index][0]
        position = index

        while position > 0 and alist[position-1][0] > currentvalue:
            alist[position][0] = alist[position-1][0]
            position = position-1

        alist[position][0] = currentvalue


# Initiative: All functions related to initiative order
def initiative():
    combat_number = int(input("How many in combat? "))
    initiative_heap = []

    for i in range(combat_number):
        mon_type = input("Type: ")
        name = input("Name: ")
        init = int(input("Initiative: "))
        print()
        heappush(initiative_heap, (init*-1, [name, mon_type]))

    tmp = []
    for i in range(len(initiative_heap)):
        tmp.append(heappop(initiative_heap))
    initiative_heap = tmp

    for i in range(len(initiative_heap)):
        initiative_heap[i] = [initiative_heap[i][0] * -1, initiative_heap[i][1][0], initiative_heap[i][1][1]]

    return initiative_heap


def change_initiative(order):
    pos = -1
    print(order)
    name = input("Who to change? ")
    for i in range(len(order)):
        if order[i][1] == name:
            pos = i
            print("found")
            break

    direction = input("DOWN or UP? ")
    change = int(input("Move how many positions? "))

    if direction == "DOWN":
        new_pos = pos + change
        tmp = order.pop(pos)
        order.insert(new_pos, tmp)
    else:
        new_pos = pos - change
        tmp = order.pop(pos)
        order.insert(new_pos, tmp)
    print(order)


# Damage: All functions related to dealing damage
def roll_dice_string(string):
    tmp = string.split("+")
    if len(tmp) != 2:
        print("Oops, there's too many dice for me to handle. Please roll manually using function.")
        return "Sorry, no "
    dice = tmp[0]
    bonus = int(tmp[1])

    total = bonus
    for _ in range(int(dice[0])):
        total += randint(1, int(dice[2:]))
    return total


def roll_dice_input():
    tmp = input("Input dice + bonus using given format (e.g. 4d6+5) ")
    tmp = tmp.split("+")
    dice = tmp[0]
    bonus = int(tmp[1])

    total = bonus
    for _ in range(int(dice[0])):
        total += randint(1, int(dice[2:]))

    return total


def deal_damage(order):
    i = 0
    for monster in order:
        if len(monster) == 4:
            print(i, monster[1])
        i += 1

    target = int(input("Deal damage to which target? "))
    damage = int(input("How much damage is being dealt? "))
    order[target][3] -= damage
    print(order[target][1], "is on", order[target][3], "hp")

    if order[target][3] < 0:
        print("They're down! Removing from initiative order.")
        order.pop(target)

    return order


# Monsters: All functions related to monsters and their information.
def create_monster_dict():
    monsters = dict()

    with open('5e-SRD-Monsters.json') as data_file:
        data = json.load(data_file)
        count = len(data) - 1

    monster_file = open('5e-SRD-Monsters.json')
    monster_json_str = monster_file.read()
    for i in range(count):
        monster_json_data = json.loads(monster_json_str)[i]
        monsters[monster_json_data['name']] = monster_json_data

    return monsters


def start_monster_health(monsters, order):
    for i in range(len(order)):
        try:
            len(monsters[order[i][2]])
            health = monsters[order[i][2]]["hit_points"]
            order[i].append(health)
        except KeyError:
            pass


def print_monster_stats(monsters, type):
    try:
        # basics
        print(monsters[type]["name"])
        print(monsters[type]["size"])
        print(monsters[type]["armor_class"])
        print(monsters[type]["speed"])

        # stats
        print("STR:", monsters[type]["strength"])
        print("DEX:", monsters[type]["dexterity"])
        print("CON:", monsters[type]["constitution"])
        print("INT:", monsters[type]["intelligence"])
        print("WIS:", monsters[type]["wisdom"])
        print("CHA", monsters[type]["charisma"])
        print()

        try:
            len(monsters[type]["special_abilities"])
            print("Special Abilities:")
            for i in range(len(monsters[type]["special_abilities"])):
                print(monsters[type]["special_abilities"][i]["name"])
                print(monsters[type]["special_abilities"][i]["desc"])
                print()
        except KeyError:
            pass
    except KeyError:
        print("No valid type given!\n")
        return


def print_monster_abilities(monsters, type):
    try:
        len(monsters[type])
        try:
            len(monsters[type]["actions"])
            print("Actions:")
            for i in range(len(monsters[type]["actions"])):
                print(monsters[type]["actions"][i]["name"])
                print(monsters[type]["actions"][i]["desc"])
                if monsters[type]["actions"][i]["attack_bonus"] != 0:
                    print(monsters[type]["actions"][i]["attack_bonus"])
                try:
                    print(monsters[type]["actions"][i]["damage_dice"])
                    print(monsters[type]["actions"][i]["damage_bonus"])
                except KeyError:
                    pass
                print()
        except KeyError:
            pass

        try:
            len(monsters[type]["legendary_actions"])
            print("\nLegendary Actions:")
            for i in range(len(monsters[type]["legendary_actions"])):
                print(monsters[type]["legendary_actions"][i]["name"])
                print(monsters[type]["legendary_actions"][i]["desc"])
                print()
        except KeyError:
            pass
    except KeyError:
        print("No valid type given!\n")
        return


def monster_choose_attack(monsters, type):
    try:
        len(monsters[type])
        try:
            len(monsters[type]["actions"])
            print("Actions:")
            for i in range(len(monsters[type]["actions"])):
                if monsters[type]["actions"][i]["attack_bonus"] != 0:
                    print(i, monsters[type]["actions"][i]["name"])
                    print("Description:", monsters[type]["actions"][i]["desc"])
                    print("Attack Bonus: +", monsters[type]["actions"][i]["attack_bonus"])
                    try:
                        print("Damage:", monsters[type]["actions"][i]["damage_dice"], "+", monsters[type]["actions"][i]["damage_bonus"])
                    except KeyError:
                        pass
                    print()

            choice = int(input("Which attack do you want? "))
            dice = monsters[type]["actions"][choice]["damage_dice"]
            dice += "+"
            dice += str(monsters[type]["actions"][choice]["damage_bonus"])
            print(dice)
            result = roll_dice_string(dice)
            print(result, "damage dealt!")
        except KeyError:
            pass
    except KeyError:
        print("No valid actions possible!\n")
        return

def monster_heal(order):
    i = 0
    for monster in order:
        if len(monster) == 4:
            print(i, monster[1])
        i += 1

    target = int(input("Heal which target? "))
    heal = int(input("How much hp to heal? "))
    order[target][3] += heal
    print(order[target][1], "is on", order[target][3], "hp")

    if order[target][3] < 0:
        print("They're down! Removing from initiative order.")
        order.pop(target)

    return order


# Primary function which all other functions are called from
def combat():
    monsters = create_monster_dict()
    order = initiative()
    start_monster_health(monsters, order)

    options = ["Next Turn", "Roll Dice", "Deal Damage to a Monster", "Display Current Monster Stats",
               "Display Current Monster Actions", "Choose Current Monster Action", "Change A Combatant's Initiative"]

    i = 0
    while True:
        print(order)
        flag = True

        while flag:
            print()
            print(order[i][1], "is up!")
            if len(order[i]) == 4:
                print("They have", order[i][3], "hp")
            print_list(options)
            print("-1", "End")
            try:
                choice = int(input("What do you want to do? "))
            except ValueError:
                choice = -2
                pass
            if choice == 0:
                flag = False
            elif choice == 1:
                print("Result:", roll_dice_input())
            elif choice == 2:
                order = deal_damage(order)
            elif choice == 3:
                print_monster_stats(monsters, order[i][2])
            elif choice == 4:
                print_monster_abilities(monsters, order[i][2])
            elif choice == 5:
                monster_choose_attack(monsters, order[i][2])
            elif choice == 6:
                change_initiative(order)

            elif choice == -1:
                return

        i += 1
        if i == len(order):
            i = 0
        print()

combat()


