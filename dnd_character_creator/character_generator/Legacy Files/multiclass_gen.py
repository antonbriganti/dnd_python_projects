__author__ = 'AntonBriganti'
from character_generator import *


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
        multi_class(p_class, ability_score, True, True)
        print('With these stats!')
        print('STR: ' + str(ability_score[0]))
        print('DEX: ' + str(ability_score[1]))
        print('CON: ' + str(ability_score[2]))
        print('INT: ' + str(ability_score[3]))
        print('WIS: ' + str(ability_score[4]))
        print('CHA: ' + str(ability_score[5]))
        tmp = input()


