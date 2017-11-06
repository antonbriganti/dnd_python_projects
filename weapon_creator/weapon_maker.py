import random, json, pprint

class WeaponFactory:
    def __init__(self):
        with open("abilities.json") as ability_json, open("melee_weapons.json") as melee_json:
            self.abilities = json.load(ability_json)
            self.weapons = json.load(melee_json)

    def create_weapon(self):
        weapon_data = random.choice(self.weapons)
        weapon = Weapon(weapon_data["weapon_name"], weapon_data["damage_dice"], weapon_data["damage_type"], weapon_data["properties"])
        return weapon

    def create_weapon_with_abilities(self, ability_count):
        weapon = self.create_weapon()
        for _ in range(ability_count):
            weapon.add_weapon_ability(random.choice(self.abilities))
        return weapon


class Weapon:
    def __init__(self, weapon_name, damage_dice, damage_type, properties):
        self.name = weapon_name
        self.damage_dice = damage_dice
        self.damage_type = damage_type
        self.properties = properties

        self.ability_limit = 2
        self.ability_prefix_set = False
        self.ability_suffix_set = False
        self.ability_descriptions = []

    def add_weapon_ability(self, ability):
        if self.under_max_ability_count:
            self.ability_descriptions.append(ability["description"])
        self.expand_name_with_ability(ability)

    def under_max_ability_count(self):
        return len(self.ability_descriptions) < self.ability_limit

    def expand_name_with_ability(self, ability):
        possibilities = []
        if not self.ability_prefix_set: possibilities.append("prefix")
        if not self.ability_suffix_set: possibilities.append("suffix")
        choice = random.choice(possibilities)

        if choice == "prefix":
            self.ability_prefix_set = True
            self.name = ability["prefix"] + " " + self.name
        elif choice == "suffix":
            self.ability_suffix_set = True
            self.name = self.name + ' ' + ability["suffix"]

weapon_forge = WeaponFactory()
pprint.pprint(weapon_forge.create_weapon_with_abilities(2).__dict__)
