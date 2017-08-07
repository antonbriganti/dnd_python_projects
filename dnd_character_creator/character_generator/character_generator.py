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

    def set_extra_racial(self, subrace_points):
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
        #STR/DEX/CON/INT/WIS/CHA
        #race : [subrace, subrace points]
        race_list = {
                    'Dwarf' : [['Hill', [0, 0, 2, 0, 1, 0]], ['Mountain', [2, 0, 2, 0, 0, 0]]],
                    'Elf' : [['High', [0, 2, 0, 1, 0, 0]], ['Wood', [0, 2, 0, 0, 1, 0]], ['Dark', [0, 2, 0, 0, 0, 1]]],
                    'Halfling' : [['Lightfoot', [0, 2, 0, 0, 0, 1]], ['Stout', [0, 2, 1, 0, 0, 0]]],
                    'Human' : [['', [1, 1, 1, 1, 1, 1]]],
                    'Dragonborn' : [['Black', [2, 0, 0, 0, 0, 1]], ['Blue', [2, 0, 0, 0, 0, 1]], ['Brass', [2, 0, 0, 0, 0, 1]],
                                    ['Bronze', [2, 0, 0, 0, 0, 1]], ['Copper', [2, 0, 0, 0, 0, 1]], ['Gold', [2, 0, 0, 0, 0, 1]],
                                    ['Green', [2, 0, 0, 0, 0, 1]], ['Red', [2, 0, 0, 0, 0, 1]], ['Silver', [2, 0, 0, 0, 0, 1]],
                                    ['White', [2, 0, 0, 0, 0, 1]]],
                    'Gnome' : [['Forest', [0, 1, 0, 2, 0, 0]], ['Rock', [0, 0, 1, 2, 0, 0]]],
                    'Half Elf' : [['', [0, 0, 0, 0, 0, 2]]],
                    'Half Orc' : [['', [2, 0, 1, 0, 0, 0]]],
                    'Tiefling' : [['', [0, 0, 0, 1, 0, 2]]]
                    }


        #class: [subclass, optimised build]
        class_list = {
                      'Barbarian' : [['Berserker', [0, 2]], ['Totem (Bear)', [0, 2]], ['Totem (Eagle)', [0, 2]], ['Totem (Wolf)', [0, 2]]],
                      'Bard' : [['College of Lore', [5, 1]], ['Collage of Valor', [5, 1]]],
                      'Cleric' : [['Knowledge', [4, 2, 0]], ['Life', [4, 2, 0]], ['Light', [4, 2, 0]],
                                  ['Nature', [4, 2, 0]], ['Tempest',[4, 2, 0]], ['Trickery', [4, 2, 0]], ['War', [4, 2, 0]]],
                      'Druid' : [['Circle of the Land', [4, 2]], ['Circle of the Moon', [4, 2]]],
                      'Fighter' : [['Champion', [0, 2, 1]], ['Battle Master', [0, 2, 1]], ['Eldritch Knight', [0, 3, 2, 1]]],
                      'Monk' : [['Way of the Open Hand', [1, 4]], ['Way of Shadow', [1, 4]],  ['Way of the Four Elements', [1, 4]]],
                      'Paladin' : [['Oath of Devotion', [0, 5]], ['Oath of the Ancients', [0, 5]], ['Oath of Vengeance', [0, 5]]],
                      'Ranger' : [['Hunter', [1, 4]], ['Beast Master', [1, 4]]],
                      'Rogue' : [['Thief', [1]], ['Assassin', [1, 5]], ['Arcane Trickster', [1, 3]]],
                      'Sorcerer' : [['Draconic Bloodline', [5, 2]], ['Wild Magic', [5, 2]]],
                      'Warlock' : [['Archfey', [5, 2]], ['Fiend', [5, 2]], ['Great Old One', [5, 2]]],
                      'Wizard': [['Abjuration', [3, 2, 1]], ['Conjuration', [3, 2, 1]], ['Divination', [3, 2, 1]],
                                  ['Enchantment', [3, 2, 5]], ['Evocation', [3, 2, 1]], ['Illusion', [3, 2, 1]], ['Necromancy', [3, 2, 1]],
                                 ['Transmutation', [3, 2, 1]]]
                      }


        # expansion data
        expansion_races = [
                           ['Aarakocra', ['', [0, 2, 0, 0, 1, 0]]],
                           ['Gensai', ['Air', [0, 1, 2, 0, 0, 0]], ['Earth', [1, 0, 2, 0, 0, 0]],
                                      ['Fire', [0, 0, 2, 1, 0, 0]], ['Water', [0, 0, 2, 0, 1, 0]]],
                           ['Goliath', ['', [2, 0, 1, 0, 0, 0]]],
                           ['Aasimar', ['Protector', [0, 0, 0, 0, 1, 2]], ['Scourge', [0, 0, 1, 0, 0, 2]], ['Fallen', [1, 0, 0, 0, 0, 2]]],
                           ['Firbolg', ['', [1, 0, 0, 0, 2, 0]]],
                           ['Kenku', ['', [0, 2, 0, 0, 1, 0]]],
                           ['Lizardfolk', ['', [0, 0, 2, 0, 1, 0]]],
                           ['Tabaxi', ['', [0, 2, 0, 0, 0, 1]]],
                           ['Triton', ['', [1, 0, 1, 0, 0, 1]]],
                           ['Bugbear', ['', [2, 1, 0, 0, 0, 0]]],
                           ['Goblin', ['', [0, 2, 1, 0, 0, 0]]],
                           ['Hobgoblin', ['', [0, 0, 2, 1, 0, 0]]],
                           ['Kobold', ['', [-2, 2, 0, 0, 0, 0]]],
                           ['Orc', ['', [2, 0, 1, -2, 0, 0]]],
                           ['Yuan Ti Pureblood', ['', [0, 0, 0, 1, 0, 2]]]
                          ]

        expansion_subraces = [
                              ["Dwarf", ['Duergar', [1, 0, 2, 0, 0, 0]]],
                              ["Gnome", ['Deep', [0, 1, 0, 2, 0, 0]]],
                              ["Tiefling", ['Feral', [0, 2, 0, 1, 0, 0]]]
                             ]

        expansion_subclass = [
                              ["Barbarian", ['Battlerager', [0, 2]], ['Totem (Elk)', [0, 2]], ['Totem (Tiger)', [0, 2]]],
                              ["Cleric", ['Arcana', [4, 2, 0]]],
                              ["Fighter", ['Purple Dragon Knight', [0, 2, 1]]],
                              ["Monk", ['Way of the Long Death', [1, 4]], ['Way of the Sun Soul', [1, 4]]],
                              ["Paladin", ['Oath of the Crown', [0, 5]]],
                              ["Rogue", ['Mastermind', [1, 3]], ['Swashbuckler', [1, 5]]],
                              ["Sorcerer", ['Storm Sorcery', [5, 2]]],
                              ["Warlock", ['Undying', [5, 2]]],
                              ["Wizard, ", ['Bladeslinger', [3, 2, 1]]]
                             ]

        if self.expansion:
            for race in expansion_races:
                race_list[race[0]] = []
                for i in range(1, len(race)):
                    race_list[race[0]].append(race[i])

            for subrace in expansion_subraces:
                for i in range(1, len(subrace)):
                    race_list[subrace[0]].append(subrace[i])

            for subclass in expansion_subclass:
                for i in range(1, len(subclass)-1):
                    class_list[subclass[0]].append(subclass[i])

        # homebrew data
        homebrew_classes = ["Blood Hunter"]
        homebrew_subclasses = [
                               ['Bard', ['College of the Maestro', [5, 1]]],
                               ["Fighter", ['Gunslinger', [1, 2]]],
                               ["Blood Hunter", ['Order of the Mutant', [0, 4]], ['Order of the Ghostslayer', [0, 4]],
                                                ['Order of the Profane Soul', [0, 4]], ['Order of the Lycan', [0, 4]]]
                              ]


        if self.homebrew:
            for h_class in homebrew_classes:
                class_list[h_class] = []

            for subclass in homebrew_subclasses:
                for i in range(1, len(subclass)):
                    class_list[subclass[0]].append(subclass[i])

        background_list = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit',
                           'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

        # random select of race/subrace
        char_race = choice(list(race_list.keys())) # randomly choose from dictionary keys as race
        char_subrace, racial_bonus = choice(race_list[char_race]) # randomly choose subrace and build

        # random select of class/subclass
        char_class = choice(list(class_list.keys()))
        char_subclass, build = choice(class_list[char_class])

        # background select
        char_background = background_list[randint(0, len(background_list)-1)]

        # sorted rolls
        if self.optimise:
            roll = self.sorted_abilities()
            ability_list = [0, 0, 0, 0, 0, 0]

            #iterates through build, adds best roll to given index
            for x in range(len(build)):
                ability_list[build[x]] += roll[0]
                roll.pop(0)

            #adds remaining rolls to ability scores randomly
            ability_count = len(build) #count of abilities set
            set_abilities = list(build) #abilities already set

            while ability_count < 6:
                ind = randint(0, len(ability_list)-1)
                if ind not in set_abilities:
                    ability_list[ind] += roll[0]
                    roll.pop(0)
                    set_abilities.append(ind)
                    ability_count += 1

        else:
            ability_list = self.initial_abilities()


        # racial bonus
        if char_race == "Half Elf":
            racial_bonus = self.set_extra_racial(racial_bonus) # set random extra ability

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

        print()
        #self.name = input('What is their name? ')
        self.print_character()

    def print_character(self):
            print()
            #print(self.name)
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

char = Character(True, True, True, False)
while True:
    char.char_generator()
