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

        self.ability_list = {
                    'STR' : 0,
                    'DEX' : 0,
                    'CON' : 0,
                    'INT' : 0,
                    'WIS' : 0,
                    'CHA' : 0
                    }

    def print_list(self, lst):
        ind = 0
        for item in lst:
            print(ind, lst[ind])
            ind += 1

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
        # 'roll' 4d6
        roll_list = [randint(1,6) for i in range(4)]

        # drop lowest dice roll
        roll_list.sort()
        roll_list.pop(0)

        return sum(roll_list)

    def unsorted_rolls(self):
        return [self.dice_roll() for i in range(6)]

    def sorted_rolls(self):
        return sorted(self.unsorted_rolls())

    def set_extra_racial(self, subrace_bonus):
        stat = choice(list(set(self.ability_list.keys()) - set(subrace_bonus)))
        subrace_bonus.append((stat, 1))
        return subrace_bonus

    def char_generator(self):
        #STR/DEX/CON/INT/WIS/CHA
        #race : [subrace, subrace points]
        race_list = {
                    'Dwarf' : [['Hill', [("CON", 2), ("WIS", 1)]], ['Mountain', [("STR", 2), ("CON", 2)]]],
                    'Elf' : [['High', [("DEX", 2), ("INT", 1)]], ['Wood', [("DEX", 2), ("WIS", 1)]], ['Dark', [("DEX", 2), ("CHA", 1)]]],
                    'Halfling' : [['Lightfoot', [("DEX", 2), ("CHA", 1)]], ['Stout', [("DEX", 2), ("CON", 1)]]],
                    'Human' : [['', [("STR", 1), ("DEX", 1), ("CON", 1), ("INT", 1), ("WIS", 1), ("CHA", 1)]]],
                    'Dragonborn' : [['Black', [("STR", 2), ("CHA", 1)]], ['Blue', [("STR", 2), ("CHA", 1)]], ['Brass', [("STR", 2), ("CHA", 1)]],
                                    ['Bronze', [("STR", 2), ("CHA", 1)]], ['Copper', [("STR", 2), ("CHA", 1)]], ['Gold', [("STR", 2), ("CHA", 1)]],
                                    ['Green', [("STR", 2), ("CHA", 1)]], ['Red', [("STR", 2), ("CHA", 1)]], ['Silver', [("STR", 2), ("CHA", 1)]],
                                    ['White', [("STR", 2), ("CHA", 1)]]],
                    'Gnome' : [['Forest', [('DEX', 1), ("INT", 2)]], ['Rock', [("CON", 1), ("INT", 2)]]],
                    'Half Elf' : [['', [("CHA", 2)]]],
                    'Half Orc' : [['', [("STR", 2), ("CON", 1)]]],
                    'Tiefling' : [['', [("INT", 1), ("CHA", 2)]]]
                    }


        #class: [subclass, optimised build]
        class_list = {
                      'Barbarian' : [['Berserker', ["STR", "CON"]], ['Totem (Bear)', ["STR", "CON"]], ['Totem (Eagle)', ["STR", "CON"]], ['Totem (Wolf)', ["STR", "CON"]]],
                      'Bard' : [['College of Lore', ["CHA", "DEX"]], ['Collage of Valor', ["CHA", "DEX"]]],
                      'Cleric' : [['Knowledge', ["WIS", "CON", "STR"]], ['Life', ["WIS", "CON", "STR"]], ['Light', ["WIS", "CON", "STR"]],
                                  ['Nature', ["WIS", "CON", "STR"]], ['Tempest',["WIS", "CON", "STR"]], ['Trickery', ["WIS", "CON", "STR"]], ['War', ["WIS", "CON", "STR"]]],
                      'Druid' : [['Circle of the Land', ["WIS", "CON"]], ['Circle of the Moon', ["WIS", "CON"]]],
                      'Fighter' : [['Champion', ["STR", "CON", "DEX"]], ['Battle Master', ["STR", "CON", "DEX"]], ['Eldritch Knight', ["STR", "INT", "CON", "DEX"]]],
                      'Monk' : [['Way of the Open Hand', ["DEX", "WIS"]], ['Way of Shadow', ["DEX", "WIS"]],  ['Way of the Four Elements', ["DEX", "WIS"]]],
                      'Paladin' : [['Oath of Devotion', ["STR", "CHA"]], ['Oath of the Ancients', ["STR", "CHA"]], ['Oath of Vengeance', ["STR", "CHA"]]],
                      'Ranger' : [['Hunter', ["DEX", "WIS"]], ['Beast Master', ["DEX", "WIS"]]],
                      'Rogue' : [['Thief', ["DEX"]], ['Assassin', ["DEX", "CHA"]], ['Arcane Trickster', ["DEX", "INT"]]],
                      'Sorcerer' : [['Draconic Bloodline', ["CHA", "CON"]], ['Wild Magic', ["CHA", "CON"]]],
                      'Warlock' : [['Archfey', ["CHA", "CON"]], ['Fiend', ["CHA", "CON"]], ['Great Old One', ["CHA", "CON"]]],
                      'Wizard': [['Abjuration', ["INT", "CON", "DEX"]], ['Conjuration', ["INT", "CON", "DEX"]], ['Divination', ["INT", "CON", "DEX"]],
                                  ['Enchantment', ["INT", "CON", "DEX"]], ['Evocation', ["INT", "CON", "DEX"]], ['Illusion', ["INT", "CON", "DEX"]],
                                  ['Necromancy', ["INT", "CON", "DEX"]], ['Transmutation', ["INT", "CON", "DEX"]]]
                      }


        # expansion data
        expansion_races = [
                           ['Aarakocra', ['', [("DEX", 2), ("WIS", 1)]]],
                           ['Gensai', ['Air', [("DEX", 1), ("CON", 2)]], ['Earth', [("STR", 1), ("CON", 2)]],
                                      ['Fire', [("INT", 1), ("CON", 2)]], ['Water', [("WIS", 1), ("CON", 2)]]],
                           ['Goliath', ['', [("STR", 2), ("CON", 1)]]],
                           ['Aasimar', ['Protector', [("WIS", 1), ("CHA", 2)]], ['Scourge', [("CON", 1), ("CHA", 2)]], ['Fallen', [("STR", 1), ("CHA", 2)]]],
                           ['Firbolg', ['', [("STR", 1), ("WIS", 2)]]],
                           ['Kenku', ['', [("DEX", 2), ("WIS", 1)]]],
                           ['Lizardfolk', ['', [("WIS", 1), ("CON", 2)]]],
                           ['Tabaxi', ['', [("DEX", 2), ("CHA", 1)]]],
                           ['Triton', ['', [("STR", 1), ("CON", 1), ("CHA", 1)]]],
                           ['Bugbear', ['', [("STR", 2), ("DEX", 1)]]],
                           ['Goblin', ['', [("DEX", 2), ("CON", 1)]]],
                           ['Hobgoblin', ['', [("CON", 2), ("INT", 1)]]],
                           ['Kobold', ['', [("STR", -2), ("DEX", 2)]]],
                           ['Orc', ['', [("STR", 2), ("CON", 1), ("INT", -2)]]],
                           ['Yuan Ti Pureblood', ['', [("INT", 1), ("CHA", 2)]]]
                          ]

        expansion_subraces = [
                              ["Dwarf", ['Duergar', [("STR", 1), ("CON", 2)]]],
                              ["Gnome", ['Deep', [("DEX", 1), ("CON", 2)]]],
                              ["Tiefling", ['Feral', [("DEX", 2), ("INT", 1)]]]
                             ]

        expansion_subclass = [
                              ["Barbarian", ['Battlerager', ["STR", "CON"]], ['Totem (Elk)', ["STR", "CON"]], ['Totem (Tiger)', ["STR", "CON"]]],
                              ["Cleric", ['Arcana', ["WIS", "CON", "STR"]]],
                              ["Fighter", ['Purple Dragon Knight', ["STR", "CON", "DEX"]]],
                              ["Monk", ['Way of the Long Death', ["DEX", "WIS"]], ['Way of the Sun Soul', ["DEX", "WIS"]]],
                              ["Paladin", ['Oath of the Crown', ["STR", "CHA"]]],
                              ["Rogue", ['Mastermind', ["DEX", "INT"]], ['Swashbuckler', ["DEX", "CHA"]]],
                              ["Sorcerer", ['Storm Sorcery', ["CHA", "CON"]]],
                              ["Warlock", ['Undying', ["CHA", "CON"]]],
                              ["Wizard, ", ['Bladeslinger', ["INT", "CON", "DEX"]]]
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
                               ['Bard', ['College of the Maestro', ["CHA", "DEX"]]],
                               ["Fighter", ['Gunslinger', ["DEX", "INT"]]],
                               ["Blood Hunter", ['Order of the Mutant', ["STR", "WIS"]], ['Order of the Ghostslayer', ["STR", "WIS"]],
                                                ['Order of the Profane Soul', ["STR", "WIS"]], ['Order of the Lycan', ["STR", "WIS"]]]
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
        char_background = choice(background_list)

        # sorted rolls
        if self.optimise:
            unallocated_points = self.sorted_rolls()

            #iterates through build, adds best roll to given index
            for ability in build:
                self.ability_list[ability] += unallocated_points.pop(0)

            #adds remaining rolls to ability scores randomly
            remaining_abilities = list(set(self.ability_list.keys()) - set(build))
            shuffle(remaining_abilities)

            for stat in remaining_abilities:
                self.ability_list[stat] += unallocated_points.pop(0)


        else:
            roll = self.unsorted_rolls()
            for key in self.ability_list.keys(): self.ability_list[key] += roll.pop(0)


        # racial bonus
        if char_race == "Half Elf":
            for _ in range(2):
                racial_bonus = self.set_extra_racial(racial_bonus) # set random extra ability

        for bonus in racial_bonus:
            self.ability_list[bonus[0]] += bonus[1]

        self.s_race = char_subrace
        self.m_race = char_race
        self.background = char_background
        self.s_class = (char_subclass)
        self.m_class = (char_class)

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
            print('STR: ' + str(self.ability_list["STR"]))
            print('DEX: ' + str(self.ability_list["DEX"]))
            print('CON: ' + str(self.ability_list["CON"]))
            print('INT: ' + str(self.ability_list["INT"]))
            print('WIS: ' + str(self.ability_list["WIS"]))
            print('CHA: ' + str(self.ability_list["CHA"]))
            input('Press Enter to continue. ')
            print()


while True:
    char = Character(True, True, True, False)
    char.char_generator()
