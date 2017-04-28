__author__ = 'AntonBriganti'

from random import *


class Character:
    def __init__(self, optimise, expansion, homebrew, usermade):
        self.name = None
        self.m_race = None
        self.s_race = None
        self.m_class = None
        self.s_class = None
        self.background = None
        self.level = 3

        self.optimise = optimise
        self.expansion = expansion
        self.homebrew = homebrew
        self.usermade = usermade

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    def print_list(self, lst):
        ind = 0
        for item in lst:
            print(ind, lst[ind])
            ind += 1

    def vowel_check(self, string, capital):
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

    def input_loop(self, lst, prompt):
        flag = True
        while flag:
            self.print_list(lst)
            try:
                ind = int(input(prompt))
            except ValueError:
                ind = -1

            if 0 <= ind <= len(lst):
                return ind

            print('Bad input, try again. \n')

    def dice_roll(self):
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

    def initial_abilities(self):
        ability_list = []

        for _ in range(6):
            ability_list.append(self.dice_roll())

        return ability_list

    def sorted_abilities(self):
        ability_list = self.initial_abilities()

        for i in range(1, len(ability_list)):
            tmp = ability_list[i]
            k = i
            while k > 0 and tmp > ability_list[k - 1]:
                ability_list[k] = ability_list[k - 1]
                k -= 1
            ability_list[k] = tmp

        return ability_list

    def set_extra(self, subrace_points):
        ind = randint(0, 4)
        subrace_points[ind] += 1

        flag = False
        while not flag:
            new = randint(0, 4)
            if new != ind:
                subrace_points[new] += 1
                flag = True

        return subrace_points

    def char_generator(self):
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

        if self.expansion:
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

        if self.homebrew:
            for h_class in homebrew_classes:
                class_list.append(h_class)
                subclass_list.append([])
                subclass_builds.append([])
            for subclass in homebrew_subclasses:
                subclass_list[subclass[0]].append(subclass[1])
                subclass_builds[subclass[0]].append(subclass[2])

        background_list = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit',
                           'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

        if self.usermade:
            # select of race/subrace
            race_ind = self.input_loop(race_list, 'Choose a race by index: ')
            char_race = race_list[race_ind]
            print()

            if len(subrace_list[race_ind]) == 1:
                subrace_ind = 0
            else:
                subrace_ind = self.input_loop(subrace_list[race_ind], 'Choose a subrace by index: ')
            char_subrace = subrace_list[race_ind][subrace_ind]
            print()

            # select of class/subclass
            class_ind = self.input_loop(class_list, 'Choose a class by index: ')
            char_class = class_list[class_ind]
            print()

            subclass_ind = self.input_loop(subclass_list[class_ind], 'Choose a subclass by index: ')
            char_subclass = subclass_list[class_ind][subclass_ind]

        else:
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

        # sorted rolls
        if self.optimise:
            roll = self.sorted_abilities()
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

        else:
            ability_list = self.initial_abilities()


        # racial bonus
        if race_ind == 4:
            subrace_ind = 0
        racial_bonus = subrace_stats[race_ind][subrace_ind]

        if race_ind == 6:
            racial_bonus = self.set_extra(racial_bonus)

        for i in range(len(ability_list)):
            ability_list[i] += racial_bonus[i]

        self.s_race = char_subrace
        self.m_race = char_race
        self.background = char_background
        self.s_class = (char_subclass)
        self.m_class = (char_class)

        self.strength = ability_list[0]
        self.dexterity = ability_list[1]
        self.constitution = ability_list[2]
        self.intelligence = ability_list[3]
        self.wisdom = ability_list[4]
        self.charisma = ability_list[5]
        self.abilities = ability_list

        self.classlist = class_list
        self.subclasslist = subclass_list

        print()
        self.name = input('What is their name? ')
        self.print_character()

    def print_character(self):
            print()
            print(self.name)
            if self.s_race != '':
                print(self.s_race, self.m_race)
            else:
                print(self.m_race)
            print(self.s_class, self.m_class)
            print(self.background)
            print('Level: ' + str(self.level))
            print('STR: ' + str(self.strength))
            print('DEX: ' + str(self.dexterity))
            print('CON: ' + str(self.constitution))
            print('INT: ' + str(self.intelligence))
            print('WIS: ' + str(self.wisdom))
            print('CHA: ' + str(self.charisma))
            input('Press Enter to continue. ')
            print()


class MultiCharacter:
    def __init__(self, optimise, expansion, homebrew, usermade):
        self.name = None
        self.m_race = None
        self.s_race = None
        self.level = 3
        self.background = None

        self.m_class = []
        self.s_class = []

        self.classlist = None
        self.subclasslist = None

        self.optimise = optimise
        self.expansion = expansion
        self.homebrew = homebrew
        self.usermade = usermade

        self.abilities = None
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    def print_list(self,lst):
        ind = 0
        for item in lst:
            print(ind, lst[ind])
            ind += 1

    def vowel_check(self, string, capital):
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

    def input_loop(self, lst, prompt):
        flag = True
        while flag:
            self.print_list(lst)
            try:
                ind = int(input(prompt))
            except ValueError:
                ind = -1

            if 0 <= ind <= len(lst)-1:
                return ind

            print('Bad input, try again. \n')

    def dice_roll(self):
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

    def initial_abilities(self):
        ability_list = []

        for _ in range(6):
            ability_list.append(self.dice_roll())

        return ability_list

    def sorted_abilities(self):
        ability_list = self.initial_abilities()

        for i in range(1, len(ability_list)):
            tmp = ability_list[i]
            k = i
            while k > 0 and tmp > ability_list[k - 1]:
                ability_list[k] = ability_list[k - 1]
                k -= 1
            ability_list[k] = tmp

        return ability_list

    def set_extra(self, subrace_points):
        ind = randint(0, 4)
        subrace_points[ind] += 1

        flag = False
        while not flag:
            new = randint(0, 4)
            if new != ind:
                subrace_points[new] += 1
                flag = True

        return subrace_points

    def char_generator(self):
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

        if self.expansion:
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

        if self.homebrew:
            for h_class in homebrew_classes:
                class_list.append(h_class)
                subclass_list.append([])
                subclass_builds.append([])
            for subclass in homebrew_subclasses:
                subclass_list[subclass[0]].append(subclass[1])
                subclass_builds[subclass[0]].append(subclass[2])

        background_list = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit',
                           'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

        if self.usermade:
            # select of race/subrace
            race_ind = self.input_loop(race_list, 'Choose a race by index: ')
            char_race = race_list[race_ind]
            print()

            if len(subrace_list[race_ind]) == 1:
                subrace_ind = 0
            else:
                subrace_ind = self.input_loop(subrace_list[race_ind], 'Choose a subrace by index: ')
            char_subrace = subrace_list[race_ind][subrace_ind]
            print()

            # select of class/subclass
            class_ind = self.input_loop(class_list, 'Choose a class by index: ')
            char_class = class_list[class_ind]
            print()

            subclass_ind = self.input_loop(subclass_list[class_ind], 'Choose a subclass by index: ')
            char_subclass = subclass_list[class_ind][subclass_ind]

        else:
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

        # sorted rolls
        if self.optimise:
            roll = self.sorted_abilities()
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

        else:
            ability_list = self.initial_abilities()


        # racial bonus
        if race_ind == 4:
            subrace_ind = 0
        racial_bonus = subrace_stats[race_ind][subrace_ind]

        if race_ind == 6:
            racial_bonus = self.set_extra(racial_bonus)

        for i in range(len(ability_list)):
            ability_list[i] += racial_bonus[i]

        self.s_race = char_subrace
        self.m_race = char_race
        self.background = char_background
        self.s_class.append(char_subclass)
        self.m_class.append(char_class)

        self.strength = ability_list[0]
        self.dexterity = ability_list[1]
        self.constitution = ability_list[2]
        self.intelligence = ability_list[3]
        self.wisdom = ability_list[4]
        self.charisma = ability_list[5]
        self.abilities = ability_list

        self.classlist = class_list
        self.subclasslist = subclass_list

        #self.name = input('What is their name? ')
        self.name = 'Test Subject'
        self.print_character()

    def check_req(self, reqs, abilities):
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

    def multi_class(self):
        #must have proper class design here, not just passing in class element into function
        multi_requirements = [[0], [5], [4], [4],
                              [True, 0, 1],
                              [1, 4], [0, 5], [0, 4],
                              [1], [5], [5], [3]]

        if self.homebrew:
            multi_requirements.append([True, 0, 1, 3])

        possible = []
        act_possible = []
        for i in range(len(self.classlist)):
            flag = True
            for mclass in self.m_class:
                if mclass == self.classlist[i]:
                    flag = False
            if self.check_req(multi_requirements[i], self.abilities) and flag:
                act_possible.append([i, self.classlist[i]])
                possible.append(self.classlist[i])

        mu_ind = self.input_loop(possible, 'Choose a class to multiclass into: ')
        mu_class = self.classlist[act_possible[mu_ind][0]]
        print()

        mu_ind2 = self.input_loop(self.subclasslist[act_possible[mu_ind][0]], "Choose a subclass: ")
        mu_subclass = self.subclasslist[act_possible[mu_ind][0]][mu_ind2]
        self.m_class.append(mu_class)
        self.s_class.append(mu_subclass)
        self.print_character()

    def print_character(self):
            print()
            print(self.name)
            if self.s_race != '':
                print(self.s_race, self.m_race)
            else:
                print(self.m_race)

            for i in range(len(self.m_class)):
                print(self.s_class[i], self.m_class[i])

            print()
            print(self.background)
            print('Level: ' + str(self.level))
            print('STR: ' + str(self.strength))
            print('DEX: ' + str(self.dexterity))
            print('CON: ' + str(self.constitution))
            print('INT: ' + str(self.intelligence))
            print('WIS: ' + str(self.wisdom))
            print('CHA: ' + str(self.charisma))
            input('Press Enter to continue. ')
            print()

    def level_up(self):
        self.level += 1

# optimise, expansion, homebrew, usermade
char = MultiCharacter(True, True, False, False)
char.char_generator()
char.print_character()
char.multi_class()
