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
        subrace_bonus.append((stat, 1))
        return subrace_bonus

    def expand_dict(self, current_dict, new_dict):
        for item in new_dict:
            if item not in current_dict:
                current_dict[item] = new_dict[item]
            else:
                for key, content in new_dict[item].items():
                    # merges conflicting items into one entry
                    current_dict[item][key] = {**current_dict[item][key], **content}
        return current_dict

    def set_races(self):
        race_list = json_reader.get_races('srd_data/phb_data.json')
        if self.runtime_flags['expansion']:
            expansion_races = json_reader.get_races("srd_data/expansion_data.json") # expansion data
            race_list = self.expand_dict(race_list, expansion_races)

        return race_list

    def set_classes(self):
        class_list = json_reader.get_classes('srd_data/phb_data.json')
        if self.runtime_flags['expansion']:
            expansion_classes = json_reader.get_classes("srd_data/expansion_data.json")
            class_list = self.expand_dict(class_list, expansion_classes)

        if self.runtime_flags['homebrew']:
            # homebrew data
            homebrew_classes = json_reader.get_classes("srd_data/homebrew_data.json")
            class_list = self.expand_dict(class_list, homebrew_classes)

        return class_list

    def set_backgrounds(self):
        background_list = json_reader.get_backgrounds('srd_data/phb_data.json')
        if self.runtime_flags['expansion']:
            expansion_backgrounds = json_reader.get_backgrounds("srd_data/expansion_data.json")
            background_list = background_list + expansion_backgrounds

        return background_list

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
        return(random.sample(set(class_skill_data["skills"]), class_skill_data["count"]))

    def char_generator(self):
        race_list = self.set_races()
        class_list = self.set_classes()
        background_list = self.set_backgrounds()

        if self.runtime_flags['usermade']:
            # select of race/subrace
            user_input = text_ui_helper.input_loop(sorted(list(race_list)), 'Choose a race by index: ')
            char_race = sorted(list(race_list))[user_input]
            print()

            if len(race_list[char_race]) == 1:
                char_subrace, racial_bonus = race_list[char_race][0]
            else:
                user_input = text_ui_helper.input_loop(race_list[char_race], 'Choose a subrace by index: ')
                print(user_input, race_list[char_race][user_input])
                char_subrace, racial_bonus = race_list[char_race][user_input]
            print()

            # select of class/subclass
            user_input = text_ui_helper.input_loop(sorted(list(class_list)), 'Choose a class by index: ')
            char_class = sorted(list(class_list))[user_input]
            print()

            user_input = text_ui_helper.input_loop(class_list[char_class], 'Choose a subclass by index: ')
            char_subclass, build = class_list[char_class][user_input]
            print()

            user_input = text_ui_helper.input_loop(background_list, 'Choose a background by index: ')
            char_background = background_list[user_input]

        else:
            # random select of race/subrace
            char_race = random.choice(list(race_list.keys())) # randomly choose from dictionary keys as race
            char_subrace, racial_bonus = random.choice(list(race_list[char_race]["subraces"].items())) # randomly choose subrace and build

            char_class = random.choice(list(class_list.keys()))
            char_subclass, build = random.choice(list(class_list[char_class]["subclasses"].items()))

            char_background = random.choice(list(background_list.keys()))

        #set stats
        if self.runtime_flags['optimise']:
            self.character.ability_list = self.set_optimised_stats(build)
        else:
            roll = stat_roller.sorted_rolls()
            for ability in self.character.ability_list.keys(): self.character.ability_list[ability] += roll.pop()

        # racial bonus
        if char_race == "Half Elf":
            for _ in range(2):
                racial_bonus = self.set_extra_racial(racial_bonus) # set random extra ability
        for bonus in racial_bonus:
            self.character.ability_list[bonus[0]] += bonus[1]

        #set proficiencies
        skill_list = background_list[char_background]["skill_proficiencies"]
        skill_list += self.set_random_class_skills(class_list[char_class]["skill_proficiencies"])

        self.character.s_race = char_subrace
        self.character.m_race = char_race
        self.character.background = char_background
        self.character.s_class = (char_subclass)
        self.character.m_class = (char_class)
        self.character.skills = skill_list

        return self.character


if __name__ == "__main__":
    #optimise, expansion, homebrew, usermade
    creator = CharacterCreator(True, False, False, False)
    char = creator.char_generator()
    char.print_character()
