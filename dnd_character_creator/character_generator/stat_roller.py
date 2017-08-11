from random import *
def dice_roll():
    # 'roll' 4d6
    roll_list = [randint(1,6) for i in range(4)]

    # drop lowest dice roll
    roll_list.sort()
    roll_list.pop(0)

    return sum(roll_list)

def unsorted_rolls():
    return [dice_roll() for i in range(6)]

def sorted_rolls():
    return sorted(unsorted_rolls())
