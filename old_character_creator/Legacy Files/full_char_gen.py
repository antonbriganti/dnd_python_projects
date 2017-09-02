__author__ = 'AntonBriganti'
from ability_gen import *

# STR/DEX/CON/INT/WIS/CHA


def set_extra(subrace_points):
    ind = randint(0, 4)
    subrace_points[ind] += 1

    flag = False
    while not flag:
        new = randint(0, 4)
        if new != ind:
            subrace_points[new] += 1
            flag = True

    return subrace_points


def pure_rng_char():
    race_list = ['Dwarf', 'Elf', 'Halfling', 'Human',
                'Dragonborn', 'Gnome', 'Half Elf', 'Half Orc', 'Tiefling']

    subrace_list = [['Hill', 'Mountain'],
                    ['High', 'Wood', 'Dark'],
                    ['Lightfoot', 'Stout'],
                    [''],
                    ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'],
                    ['Forest', 'Rock'],
                    [''],
                    [''],
                    ['']]

    #STR/DEX/CON/INT/WIS/CHA
    subrace_stats = [[[0, 0, 2, 0, 1, 0], [2, 0, 2, 0, 0, 0]],
                    [[0, 2, 0, 1, 0, 0], [0, 2, 0, 0, 1, 0], [0, 2, 0, 0, 0, 1]],
                    [[0, 2, 0, 0, 0, 1], [0, 2, 1, 0, 0, 0]],
                    [[1, 1, 1, 1, 1, 1]],
                    [[2, 0, 0, 0, 0, 1]],
                    [[0, 1, 0, 2, 0, 0], [0, 0, 1, 2, 0, 0]],
                    [[0, 0, 0, 0, 0, 2]],
                    [[2, 0, 1, 0, 0, 0]],
                    [[0, 0, 0, 1, 0, 2]]]

    class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
                  'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    subclass_list = [['Berserker', 'Totem (Bear)', 'Totem (Eagle)', 'Totem (Wolf)'],
                     ['College of Lore', 'Collage of Valor'],
                     ['Knowledge', 'Life', 'Light', 'Nature', 'Tempest', 'Trickery', 'War'],
                     ['Circle of the Land', 'Circle of the Moon'],
                     ['Champion', 'Battle Master', 'Eldritch Knight'],
                     ['Way of the Open Hand', 'Way of Shadow',  'Way of the Four Elements'],
                     ['Oath of Devotion', 'Oath of the Ancients', 'Oath of Vengeance'],
                     ['Hunter', 'Beast Master'],
                     ['Thief', 'Assassin', 'Arcane Trickster'],
                     ['Draconic Bloodline', 'Wild Magic'],
                     ['Archfey', 'Fiend', 'Great Old One'],
                     ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy',
                      'Transmutation']]

    background_list = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit',
                       'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']



    # random select of race/subrace
    # rng from 0 to size of list, save index for subrace rng creation
    race_ind = randint(0, len(race_list)-1)
    char_race = race_list[race_ind]
    subrace_ind = randint(0, len(subrace_list[race_ind])-1)
    char_subrace = subrace_list[race_ind][subrace_ind]

    # random select of class/subclass
    class_ind = randint(0, len(class_list)-1)
    char_class = class_list[class_ind]
    subclass_ind = randint(0,len(subclass_list[class_ind])-1)
    char_subclass = subclass_list[class_ind][subclass_ind]

    # background select
    char_background = background_list[randint(0, len(background_list)-1)]


    ability_list = initial_abilities()
    if race_ind == 4:
        subrace_ind = 0
    racial_bonus = subrace_stats[race_ind][subrace_ind]

    if race_ind == 6:
        racial_bonus = set_extra(racial_bonus)

    for i in range(len(ability_list)):
        ability_list[i] += racial_bonus[i]

    return char_subrace, char_race, char_background, char_subclass, char_class, ability_list


def optimised_rng_char():
    race_list = ['Dwarf', 'Elf', 'Halfling', 'Human',
                'Dragonborn', 'Gnome', 'Half Elf', 'Half Orc', 'Tiefling']

    subrace_list = [['Hill', 'Mountain'],
                    ['High', 'Wood', 'Dark'],
                    ['Lightfoot', 'Stout'],
                    [''],
                    ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'],
                    ['Forest', 'Rock'],
                    [''],
                    [''],
                    ['']]

    #STR/DEX/CON/INT/WIS/CHA
    subrace_stats = [[[0, 0, 2, 0, 1, 0], [2, 0, 2, 0, 0, 0]],
                     [[0, 2, 0, 1, 0, 0], [0, 2, 0, 0, 1, 0], [0, 2, 0, 0, 0, 1]],
                     [[0, 2, 0, 0, 0, 1], [0, 2, 1, 0, 0, 0]],
                     [[1, 1, 1, 1, 1, 1]],
                     [[2, 0, 0, 0, 0, 1]],
                     [[0, 1, 0, 2, 0, 0], [0, 0, 1, 2, 0, 0]],
                     [[0, 0, 0, 0, 0, 2]],
                     [[2, 0, 1, 0, 0, 0]],
                     [[0, 0, 0, 1, 0, 2]]]

    class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
                  'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    subclass_list = [['Berserker', 'Totem (Bear)', 'Totem (Eagle)', 'Totem (Wolf)'],
                     ['College of Lore', 'Collage of Valor'],
                     ['Knowledge', 'Life', 'Light', 'Nature', 'Tempest', 'Trickery', 'War'],
                     ['Circle of the Land', 'Circle of the Moon'],
                     ['Champion', 'Battle Master', 'Eldritch Knight'],
                     ['Way of the Open Hand', 'Way of Shadow',  'Way of the Four Elements'],
                     ['Oath of Devotion', 'Oath of the Ancients', 'Oath of Vengeance'],
                     ['Hunter', 'Beast Master'],
                     ['Thief', 'Assassin', 'Arcane Trickster'],
                     ['Draconic Bloodline', 'Wild Magic'],
                     ['Archfey', 'Fiend', 'Great Old One'],
                     ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy',
                      'Transmutation']]

    subclass_builds = [[[0, 2], [0, 2], [0, 2], [0, 2]],
                       [[5, 1], [5, 1]],
                       [[4, 2, 0], [4, 2, 0], [4, 2, 0], [4, 2, 0], [4, 2, 0], [4, 2, 0], [4, 2, 0]],
                       [[4, 2], [4, 2]],
                       [[0, 2, 1], [0, 2, 1], [0, 3, 2, 1]],
                       [[1, 4], [1, 4], [1, 4]],
                       [[0, 5], [0, 5], [0, 5]],
                       [[1, 4], [1, 4]],
                       [[1], [1,5], [1,3]],
                       [[5, 2], [5, 2]],
                       [[5, 2], [5, 2], [5,2]],
                       [[3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 5], [3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 1]]]

    background_list = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit',
                       'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']



    # random select of race/subrace
    # rng from 0 to size of list, save index for subrace rng creation
    race_ind = randint(0, len(race_list)-1)
    char_race = race_list[race_ind]
    subrace_ind = randint(0, len(subrace_list[race_ind])-1)
    char_subrace = subrace_list[race_ind][subrace_ind]

    # random select of class/subclass
    class_ind = randint(0, len(class_list)-1)
    char_class = class_list[class_ind]
    subclass_ind = randint(0,len(subclass_list[class_ind])-1)
    char_subclass = subclass_list[class_ind][subclass_ind]

    # background select
    char_background = background_list[randint(0, len(background_list)-1)]

    # get sorted rolls
    roll = sorted_abilities()
    ability_list = [0, 0, 0, 0, 0, 0]
    build = subclass_builds[class_ind][subclass_ind]

    for x in range(len(build)):
        ability_list[build[x]] += roll[0]
        roll.pop(0)

    flag = False
    while not flag:
        ind = randint(0, len(ability_list)-1)
        if ability_list[ind] == 0:
            ability_list[ind] += roll[0]
            roll.pop(0)
        for num in ability_list:
            if num != 0:
                flag = True
            else:
                flag = False
                break


    # racial bonus
    if race_ind == 4:
        subrace_ind = 0
    racial_bonus = subrace_stats[race_ind][subrace_ind]

    if race_ind == 6:
        racial_bonus = set_extra(racial_bonus)

    for i in range(len(ability_list)):
        ability_list[i] += racial_bonus[i]

    return char_subrace, char_race, char_background, char_subclass, char_class, ability_list


p_subrace, p_race, p_background, p_subclass, p_class, ability_score = optimised_rng_char()

print('Behold, your character is...')
print("A " + p_subrace + ' ' + p_race)
print("They are a " + p_background)
print("Who is a " + p_subclass + ' ' + p_class)
print('With these stats!')
print('STR: ' + str(ability_score[0]))
print('DEX: ' + str(ability_score[1]))
print('CON: ' + str(ability_score[2]))
print('INT: ' + str(ability_score[3]))
print('WIS: ' + str(ability_score[4]))
print('CHA: ' + str(ability_score[5]))
