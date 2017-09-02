__author__ = 'AntonBriganti'

from random import *


def base_char():
    race_list = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Human (Variant)',
                'Dragonborn', 'Gnome', 'Half Elf', 'Half Orc', 'Tiefling']

    subrace_list = [['Hill', 'Mountain'],
                    ['High', 'Wood', 'Dark'],
                    ['Lightfoot', 'Stout'],
                    [''],
                    [''],
                    ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'],
                    ['Forest', 'Rock'],
                    [''],
                    [''],
                    ['']]

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
    ind = randint(0, len(race_list)-1)
    char_race = race_list[ind]
    char_subrace = subrace_list[ind][randint(0,len(subrace_list[ind])-1)]

    # random select of class/subclass
    ind = randint(0, len(class_list)-1)
    char_class = class_list[ind]
    char_subclass = subclass_list[ind][randint(0,len(subclass_list[ind])-1)]

    # background select
    char_background = background_list[randint(0, len(background_list)-1)]

    if char_subrace == '':
        return char_background, char_race, char_subclass, char_class
    else:
        return char_background, char_subrace, char_race, char_subclass, char_class

print(base_char())
