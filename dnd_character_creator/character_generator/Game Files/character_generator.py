__author__ = 'antonb'

from random import *


def vowel_check(string, capital):
    if string == '':
        if capital:
            return 'A '
        else:
            return 'a '

    vowels = ['A','a','E','e', 'I', 'i', 'O', 'o', 'U', 'u']
    for char in vowels:
        if string[0] == char:
            if capital:
                return 'An '
            else:
                return 'an '
    if capital:
        return 'A '
    else:
        return 'a '


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


def pure_rng_char(expansion, homebrew):
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

    expansion_races = [['Aarakocra', [''], [0, 2, 0, 0, 1, 0]],
                       ['Gensai', ['Air', 'Earth', 'Fire', 'Water'], [[0, 1, 2, 0, 0, 0], [1, 0, 2, 0, 0, 0], [0, 0, 2, 1, 0, 0], [0, 0, 2, 0, 1, 0]]],
                       ['Goliath', [''], [2, 0, 1, 0, 0, 0]]]

    expansion_subraces = [[0, 'Duergar', [1, 0, 2, 0, 0, 0]],
                          [5, 'Deep', [0, 1, 0, 2, 0, 0]],
                          [8, 'Feral', [0, 2, 0, 1, 0, 0]]]

    expansion_subclass = [['Battlerager', 'Totem (Elk)', 'Totem (Tiger)'],
                          [],
                          ['Arcana'],
                          [],
                          ['Purple Dragon Knight'],
                          ['Way of the Long Death', 'Way of the Sun Soul'],
                          ['Oath of the Crown'],
                          [],
                          ['Mastermind', 'Swashbuckler'],
                          ['Storm Sorcery'],
                          ['Undying'],
                          ['Bladeslinger']]

    if expansion:
        for race in expansion_races:
            race_list.append(race[0])
            subrace_list.append(race[1])
            subrace_stats.append([])
            if len(race[2]) == 6:
                subrace_stats[-1].append(race[2])
            else:
                for a in range(len(race[2])):
                    subrace_stats[-1].append(race[2][a])

        for subrace in expansion_subraces:
            subrace_list[subrace[0]].append(subrace[1])
            subrace_stats[subrace[0]].append(subrace[2])

        for b in range(len(expansion_subclass)):
            if len(expansion_subclass[b]) != 0:
                for c in range(len(expansion_subclass[b])):
                    subclass_list[b].append(expansion_subclass[b][c])

    # homebrew data
    homebrew_classes = ['Blood Hunter']
    homebrew_subclasses = [[1, 'College of the Maestro', [5, 1]],
                           [4, 'Gunslinger', [1, 2]],
                           [-1, 'Order of the Mutant', [0, 4]],
                           [-1, 'Order of the Ghostslayer', [0, 4]],
                           [-1, 'Order of the Profane Soul', [0, 4]],
                           [-1, 'Order of the Lycan', [0, 4]]]

    if homebrew:
        for h_class in homebrew_classes:
            class_list.append(h_class)
            subclass_list.append([])
        for subclass in homebrew_subclasses:
            subclass_list[subclass[0]].append(subclass[1])

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


def optimised_rng_char(expansion, homebrew):
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
                       [[1], [1, 5], [1, 3]],
                       [[5, 2], [5, 2]],
                       [[5, 2], [5, 2], [5, 2]],
                       [[3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 5], [3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 1]]]

    # expansion data
    expansion_races = [['Aarakocra', [''], [0, 2, 0, 0, 1, 0]],
                       ['Gensai', ['Air', 'Earth', 'Fire', 'Water'], [[0, 1, 2, 0, 0, 0], [1, 0, 2, 0, 0, 0], [0, 0, 2, 1, 0, 0], [0, 0, 2, 0, 1, 0]]],
                       ['Goliath', [''], [2, 0, 1, 0, 0, 0]]]

    expansion_subraces = [[0, 'Duergar', [1, 0, 2, 0, 0, 0]],
                          [5, 'Deep', [0, 1, 0, 2, 0, 0]],
                          [8, 'Feral', [0, 2, 0, 1, 0, 0]]]

    expansion_subclass = [['Battlerager', 'Totem (Elk)', 'Totem (Tiger)'],
                          [],
                          ['Arcana'],
                          [],
                          ['Purple Dragon Knight'],
                          ['Way of the Long Death', 'Way of the Sun Soul'],
                          ['Oath of the Crown'],
                          [],
                          ['Mastermind', 'Swashbuckler'],
                          ['Storm Sorcery'],
                          ['Undying'],
                          ['Bladeslinger']]

    expansion_subbuild = [[[0, 2], [0, 2], [0, 2]],
                          [],
                          [[4, 2, 0]],
                          [],
                          [[0, 2, 1]],
                          [[1, 4], [1, 4]],
                          [[0, 5]],
                          [],
                          [[1], [1, 5]],
                          [[5, 2]],
                          [[5, 2]],
                          [[3, 2, 1]]]

    if expansion:
        for race in expansion_races:
            race_list.append(race[0])
            subrace_list.append(race[1])
            subrace_stats.append([])
            if len(race[2]) == 6:
                subrace_stats[-1].append(race[2])
            else:
                for a in range(len(race[2])):
                    subrace_stats[-1].append(race[2][a])

        for subrace in expansion_subraces:
            subrace_list[subrace[0]].append(subrace[1])
            subrace_stats[subrace[0]].append(subrace[2])

        for b in range(len(expansion_subclass)):
            if len(expansion_subclass[b]) != 0:
                for c in range(len(expansion_subclass[b])):
                    subclass_list[b].append(expansion_subclass[b][c])
                    subclass_builds[b].append(expansion_subbuild[b][c])

    # homebrew data
    homebrew_classes = ['Blood Hunter']
    homebrew_subclasses = [[1, 'College of the Maestro', [5, 1]],
                           [4, 'Gunslinger', [1, 2]],
                           [-1, 'Order of the Mutant', [0, 4]],
                           [-1, 'Order of the Ghostslayer', [0, 4]],
                           [-1, 'Order of the Profane Soul', [0, 4]],
                           [-1, 'Order of the Lycan', [0, 4]]]

    if homebrew:
        for h_class in homebrew_classes:
            class_list.append(h_class)
            subclass_list.append([])
            subclass_builds.append([])
        for subclass in homebrew_subclasses:
            subclass_list[subclass[0]].append(subclass[1])
            subclass_builds[subclass[0]].append(subclass[2])

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

def check_req(reqs, abilities):
    if reqs[0] is True:
        if len(reqs) == 4:
            if abilities[reqs[1]] >= 13 or abilities[reqs[2]] >= 13:
                if abilities[reqs[3]] >= 13:
                    return True
                else:
                    return False
            else:
                return False

        for i in range(1, len(reqs)):
            if abilities[reqs[i]] >= 13:
                return True
        return False

    for req in reqs:
        if abilities[req] < 13:
            return False
    return True


def multi_class(base_class, abilities, expansion, homebrew):
    class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
                  'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    # STR/DEX/CON/INT/WIS/CHA
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

    # expansion data
    expansion_subclass = [['Battlerager', 'Totem (Elk)', 'Totem (Tiger)'],
                          [],
                          ['Arcana'],
                          [],
                          ['Purple Dragon Knight'],
                          ['Way of the Long Death', 'Way of the Sun Soul'],
                          ['Oath of the Crown'],
                          [],
                          ['Mastermind', 'Swashbuckler'],
                          ['Storm Sorcery'],
                          ['Undying'],
                          ['Bladeslinger']]

    multi_requirements = [[0], [5], [4], [4],
                          [True, 0, 1],
                          [1, 4], [0, 5], [0, 4],
                          [1], [5], [5], [3]]

    if expansion:
        for b in range(len(expansion_subclass)):
            if len(expansion_subclass[b]) != 0:
                for c in range(len(expansion_subclass[b])):
                    subclass_list[b].append(expansion_subclass[b][c])


    homebrew_classes = ['Blood Hunter']
    homebrew_subclasses = [[1, 'College of the Maestro', [5, 1]],
                           [4, 'Gunslinger', [1, 3, 2]],
                           [-1, 'Order of the Mutant', [0, 4]],
                           [-1, 'Order of the Ghostslayer', [0, 4]],
                           [-1, 'Order of the Profane Soul', [0, 4]],
                           [-1, 'Order of the Lycan', [0, 4]]]

    if homebrew:
        for h_class in homebrew_classes:
            class_list.append(h_class)
            subclass_list.append([])
            multi_requirements.append([True, 0, 1, 3])
        for subclass in homebrew_subclasses:
            subclass_list[subclass[0]].append(subclass[1])

    class_ind = randint(0, len(class_list)-1)
    multi_mainclass = class_list[class_ind]

    while multi_mainclass == base_class or not check_req(multi_requirements[class_ind], abilities):
        class_ind = randint(0, len(class_list)-1)
        multi_mainclass = class_list[class_ind]

    subclass_ind = randint(0, len(subclass_list[class_ind])-1)
    multi_subclass = subclass_list[class_ind][subclass_ind]

    print("Your multiclass is... ")
    print(multi_subclass, multi_mainclass)

if __name__ == "__main__":

    tmp = ''
    while tmp == '':
        # p_subrace, p_race, p_background, p_subclass, p_class, ability_score = optimised_rng_char(True, True)
        p_subrace, p_race, p_background, p_subclass, p_class, ability_score = pure_rng_char(True, True)
        
        print('Behold, your character is...')
        print(vowel_check(p_subrace, True) + p_subrace + ' ' + p_race)
        print("They are " + vowel_check(p_background, False) + p_background)
        print("Who is " + vowel_check(p_subclass, False) + p_subclass + ' ' + p_class)
        # multi_class(p_class, ability_score, True, True)
        print('With these stats!')
        print('STR: ' + str(ability_score[0]))
        print('DEX: ' + str(ability_score[1]))
        print('CON: ' + str(ability_score[2]))
        print('INT: ' + str(ability_score[3]))
        print('WIS: ' + str(ability_score[4]))
        print('CHA: ' + str(ability_score[5]))
        tmp = input()
