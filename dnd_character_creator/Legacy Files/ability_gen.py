__author__ = 'AntonBriganti'
from random import *


def dice_roll():
    roll_list = []

    # 'roll' 4d6
    for _ in range(4):
        roll_list.append(randint(1,6))

    # drop lowest dice roll
    ind = 0
    for j in range(len(roll_list)):
        if roll_list[ind] > roll_list[j]:
            ind = j
    roll_list.pop(ind)

    # calculate total
    total = 0
    for num in roll_list:
        total += num

    return total


def initial_abilities():
    ability_list = []

    for _ in range(6):
        ability_list.append(dice_roll())

    return ability_list


def sorted_abilities():
    ability_list = initial_abilities()

    for i in range(1, len(ability_list)):
        tmp = ability_list[i]
        k = i
        while k > 0 and tmp > ability_list[k - 1]:
            ability_list[k] = ability_list[k - 1]
            k -= 1
        ability_list[k] = tmp

    return ability_list


