__author__ = 'AntonBriganti'

from random import *


def roll_health(x, mod):
    health = 0
    for _ in range(3):
        tmp = randint(1,x)
        health += tmp + mod
    return health


class Character:
    def __init__(self, name, race, subrace, main_class, subclass, abilities):
        self.name = name
        self.m_race = race
        self.s_race = subrace
        self.m_class = main_class
        self.s_class = subclass

        self.strength = abilities[0]
        self.dexterity = abilities[1]
        self.constitution = abilities[2]
        self.intelligence = abilities[3]
        self.wisdom = abilities[4]
        self.charisma = abilities[5]
        
        if self.m_class == 'Bard' or  self.m_class == 'Sorcerer' or self.m_class =='Warlock':
            self.damage_mod = self.find_mod(self.charisma)
            self.type = 'Spellcaster'

        elif self.m_class == 'Druid':
            self.damage_mod = self.find_mod(self.wisdom)
            self.type = 'Spellcaster'
            
        elif self.m_class == 'Wizard':
            self.damage_mod = self.find_mod(self.intelligence)
            self.type = 'Spellcaster'
            
        elif self.m_class == 'Ranger' or self.m_class == 'Monk':
            self.damage_mod = self.find_mod(self.dexterity)
            self.type = 'Physical'
            
        else:
            self.damage_mod = self.find_mod(self.strength)
            self.type = 'Physical'
            

        if self.m_class == 'Barbarian':
            self.health = roll_health(12, self.find_mod(self.constitution))
        elif self.m_class == 'Fighter' or self.m_class == 'Ranger':
            self.health = roll_health(10, self.find_mod(self.constitution))
        elif self.m_class == 'Sorcerer' or self.m_class == 'Wizard':
            self.health = roll_health(6, self.find_mod(self.constitution))
        else:
            self.health = roll_health(8, self.find_mod(self.constitution))

    def find_mod(self, stat):
        mod = stat - 10
        mod = mod // 2
        return mod

    def damage(self):
        return self.damage_mod

    def take_damage(self,damage):
        self.health -= damage
        print(self.name + ' got hit for ' + str(damage) + ' points of damage!')


    def dodge(self, damage):
        dex_check = self.find_mod(self.dexterity)
        chance = randint(1,6)
        if dex_check >= damage:
            if chance > 3:
                print (self.name + ' dodged!')
            else:
                print(self.name + ' went to dodge but got scraped by the attack')
                self.take_damage(damage//2)
        else:
            if chance > 5:
                print(self.name + ' barely got out of the way! ')
            else:
                print(self.name + ' completely failed to dodge')
                self.take_damage(damage)


    def special_ability(self):
        if self.type == 'Spellcaster':
            print(self.name + ' casts a devastating spell!')
            return self.damage_mod * 3
        if self.type == 'Physical':
            print(self.name + ' lunges widely, landing a crushing blow')
            return self.damage_mod + 2

    def special_dodge(self, damage, d_type):
        if d_type == 'Spellcaster':
            chance = randint(1,6)
            dex_check = self.find_mod(self.dexterity)
            if dex_check > (damage//2) - 1:
                if chance > 4:
                    print(self.name + ' somehow dodges out of the way')
                else:
                    print(self.name + " got struck, but managed to dodge some of the damage!")
                    self.take_damage(damage//2 + 1)
            else:
                print("It's no use! " + self.name + " gets consumed by the spell!")
                self.take_damage(damage)

        elif d_type == 'Physical':
            print(self.name + " didn't even get the chance to dodge the crushing blow")
            self.take_damage(damage)
            


    def enemy_choice(self):
        choice = randint(1,2)
        if choice == 1:
            return 'Attack'
        elif choice == 2:
            return 'Dodge'

