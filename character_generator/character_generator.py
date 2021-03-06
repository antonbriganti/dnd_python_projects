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

    def generate_dict(self):
        return self.__dict__

    def generate_json_string(self):
        return json.dumps(self.generate_dict())

class CharacterCreator:
    def __init__(self, optimise, expansion, homebrew, user_choice = {}):
        self.runtime_flags = {'optimise': optimise, 'expansion': expansion,
                            'homebrew': homebrew}
        self.user_choice = user_choice

    def set_extra_racial(self, current_abilities, subrace_bonus):
        stat = random.choice(list(set(current_abilities.keys()) - set(subrace_bonus)))
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
            background_list = self.expand_dict(background_list, expansion_backgrounds)

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

    def set_random_class_skills(self, class_skill_data, skill_list):
        return(random.sample(set(class_skill_data["skills"]) - set(skill_list), class_skill_data["count"]))

    def get_user_or_random_choice(self, key, dictionary):
        if key in self.user_choice and self.user_choice[key] in dictionary.keys():
            return self.user_choice[key]
        else: return random.choice(list(dictionary.keys()))

    def char_generator(self):
        character = Character()

        race_list = self.set_races()
        class_list = self.set_classes()
        background_list = self.set_backgrounds()

        # random select of race/subrace
        char_race = self.get_user_or_random_choice("m_race", race_list)
        char_subrace = self.get_user_or_random_choice("s_race", race_list[char_race]["subraces"])
        racial_bonus = race_list[char_race]["subraces"][char_subrace]

        char_class = self.get_user_or_random_choice("m_class", class_list)
        char_subclass = self.get_user_or_random_choice("s_class", class_list[char_class]["subclasses"])
        build = class_list[char_class]["subclasses"][char_subclass]

        char_background = self.get_user_or_random_choice("background", background_list)

        #set stats
        if self.runtime_flags['optimise']:
            character.ability_list = self.set_optimised_stats(build)
        else:
            roll = stat_roller.sorted_rolls()
            for ability in character.ability_list.keys(): character.ability_list[ability] += roll.pop()

        # racial bonus
        if char_race == "Half Elf":
            for _ in range(2):
                racial_bonus.append(self.set_extra_racial(character.ability_list, racial_bonus)) # set random extra ability
        for bonus in racial_bonus:
            character.ability_list[bonus[0]] += bonus[1]

        #set proficiencies
        skill_list = background_list[char_background]["skill_proficiencies"]
        skill_list += self.set_random_class_skills(class_list[char_class]["skill_proficiencies"], skill_list)

        if "name" in self.user_choice:
            character.name = self.user_choice["name"]
        character.s_race = char_subrace
        character.m_race = char_race
        character.s_class = char_subclass
        character.m_class = char_class
        character.background = char_background
        character.skills = skill_list

        return character


if __name__ == "__main__":
    #user_input = {"m_race":"Dragonborn", "s_race":"asd", "m_class":"Monk", "s_class":"Way of the Long Death"}
    creator = CharacterCreator(True, True, True)
    char = creator.char_generator()
    print(char.generate_json_string())
