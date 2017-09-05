#!/usr/local/bin/python3.6

import json, random
import json_reader, text_ui_helper, stat_roller

class Character:
    def __init__(self):
        self.name = None
        self.m_race = None
        self.s_race = None
        self.m_class = None
        self.s_class = None
        self.background = None
        self.level = 3
        self.skills = []

        self.ability_list = {
                    'STR' : 0,
                    'DEX' : 0,
                    'CON' : 0,
                    'INT' : 0,
                    'WIS' : 0,
                    'CHA' : 0
                    }

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
            print('Skill Proficiencies: ' + ', '.join(self.skills))
            #input('Press Enter to continue. ')
            print()

    def generate_json(self):
        return json.dumps(self.__dict__)

    def generate_dict(self):
        return self.__dict__

class CharacterCreator:
    def __init__(self, optimise, expansion, homebrew, usermade):
        self.character = Character()
        self.runtime_flags = {'optimise': optimise, 'expansion': expansion,
                            'homebrew': homebrew, 'usermade': usermade}

    def set_extra_racial(self, subrace_bonus):
        stat = random.choice(list(set(self.character.ability_list.keys()) - set(subrace_bonus)))
        return (stat, 1)

    def expand_dict(self, current_dict, new_dict):
        for item in new_dict:
            if item not in current_dict:
                current_dict[item] = new_dict[item]
            else:
                for key, content in new_dict[item].items():
                    current_dict[item][key].update(content) # merges conflicting items into one entry
        return current_dict

    def set_races(self):
        selectable_races = json_reader.get_races('srd_data/phb_data.json')
        if self.runtime_flags['expansion']:
            expansion_races = json_reader.get_races("srd_data/expansion_data.json") # expansion data
            selectable_races = self.expand_dict(selectable_races, expansion_races)

        return selectable_races

    def set_classes(self):
        selectable_classes = json_reader.get_classes('srd_data/phb_data.json')
        if self.runtime_flags['expansion']:
            expansion_classes = json_reader.get_classes("srd_data/expansion_data.json")
            selectable_classes = self.expand_dict(selectable_classes, expansion_classes)

        if self.runtime_flags['homebrew']:
            # homebrew data
            homebrew_classes = json_reader.get_classes("srd_data/homebrew_data.json")
            selectable_classes = self.expand_dict(selectable_classes, homebrew_classes)

        return selectable_classes

    def set_backgrounds(self):
        selectable_backgrounds = json_reader.get_backgrounds('srd_data/phb_data.json')
        if self.runtime_flags['expansion']:
            expansion_backgrounds = json_reader.get_backgrounds("srd_data/expansion_data.json")
            selectable_backgrounds = self.expand_dict(selectable_backgrounds, expansion_backgrounds)

        return selectable_backgrounds

    def set_optimised_stats(self, build):
        ability_list = {'STR' : 0, 'DEX' : 0, 'CON' : 0, 'INT' : 0, 'WIS' : 0, 'CHA' : 0}

        #iterates through build, adds best roll to given index
        unallocated_points = stat_roller.sorted_rolls()
        for ability in build:
            ability_list[ability] += unallocated_points.pop()

        #adds remaining rolls to ability scores randomly
        remaining_abilities = list(set(ability_list.keys()) - set(build))
        random.shuffle(remaining_abilities)
        for stat in remaining_abilities:
            ability_list[stat] += unallocated_points.pop()

        return ability_list

    def set_random_class_skills(self, class_skill_data):
        return(random.sample(set(class_skill_data["skills"]) - set(self.character.skills), class_skill_data["count"]))

    def char_generator(self):
        selectable_races = self.set_races()
        selectable_classes = self.set_classes()
        selectable_backgrounds = self.set_backgrounds()

        if self.runtime_flags['usermade']:
            # select of race/subrace
            user_input = text_ui_helper.input_loop(sorted(list(selectable_races)), 'Choose a race by index: ')
            self.character.m_race = sorted(list(selectable_races))[user_input]
            print()

            if len(selectable_races[self.character.m_race]["subraces"]) == 1:
                self.character.s_race = ''
            else:
                user_input = text_ui_helper.input_loop(sorted(list(selectable_races[self.character.m_race]["subraces"])), 'Choose a subrace by index: ')
                self.character.s_race = sorted(list(selectable_races[self.character.m_race]["subraces"]))[user_input]

            racial_bonus = selectable_races[self.character.m_race]["subraces"][self.character.s_race]
            print()

            # select of class/subclass
            user_input = text_ui_helper.input_loop(sorted(list(selectable_classes)), 'Choose a class by index: ')
            self.character.m_class = sorted(list(selectable_classes))[user_input]
            print()

            user_input = text_ui_helper.input_loop(sorted(list(selectable_classes[self.character.m_class]["subclasses"])), 'Choose a subclass by index: ')
            self.character.s_class = sorted(list(selectable_classes[self.character.m_class]["subclasses"]))[user_input]
            build = selectable_classes[self.character.m_class]["subclasses"][self.character.s_class]


            user_input = text_ui_helper.input_loop(sorted(list(selectable_backgrounds)), 'Choose a background by index: ')
            self.character.background = sorted(list(selectable_backgrounds))[user_input]

        else:
            # random select of race/subrace
            self.character.m_race = random.choice(list(selectable_races.keys())) # randomly choose from dictionary keys as race
            self.character.s_race, racial_bonus = random.choice(list(selectable_races[self.character.m_race]["subraces"].items())) # randomly choose subrace and build

            self.character.m_class = random.choice(list(selectable_classes.keys()))
            self.character.s_class, build = random.choice(list(selectable_classes[self.character.m_class]["subclasses"].items()))

            self.character.background = random.choice(list(selectable_backgrounds.keys()))

        #set stats
        if self.runtime_flags['optimise']:
            self.character.ability_list = self.set_optimised_stats(build)
        else:
            roll = stat_roller.sorted_rolls()
            for ability in self.character.ability_list.keys(): self.character.ability_list[ability] += roll.pop()

        # racial bonus
        if self.character.m_race == "Half Elf":
            for _ in range(2):
                racial_bonus.append(self.set_extra_racial(racial_bonus)) # set random extra ability
                
        for bonus in racial_bonus:
            self.character.ability_list[bonus[0]] += bonus[1]

        #set proficiencies
        self.character.skills = selectable_backgrounds[self.character.background]["skill_proficiencies"]
        self.character.skills += self.set_random_class_skills(selectable_classes[self.character.m_class]["skill_proficiencies"])


        return self.character


if __name__ == "__main__":
    #optimise, expansion, homebrew, usermade
    creator = CharacterCreator(True, True, True, True)
    char = creator.char_generator()
    char.print_character()
