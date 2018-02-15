#!/usr/local/bin/python3.6
import table_roller


class NPC:
    def __init__(self):
        self.appearance = table_roller.roll_table("appearance")
        self.mannerisms = table_roller.roll_table("mannerisms")
        self.interaction_behaviour = table_roller.roll_table("interactions")
        
        self.talent = table_roller.roll_table("talents")
        self.bond = table_roller.roll_table("bonds")
        self.flaw = table_roller.roll_table("flaws")
        
        # self.background = table_roller.generate_background()
        
    def print_description(self):
        print("NPC DESCRIPTION")
        print("The first thing that someone would notice about them is their " + self.appearance.lower() + ".")
        print("After talking to them for more than a brief moment, it becomes obvious that they have a habit of " + self.mannerisms.lower() + ", and are " + self.interaction_behaviour.lower() + " towards the people they talk to.")
        print()
        print("They have the remarkable talent of being able to " + self.talent.lower() + ".")
        print("As a person, they are " + self.bond.lower() + ", but they also " + self.flaw.lower() + ".")
        print()
        # print("They have a background as a " + self.background["name"] +" having become one because " + self.background["reason"])
        
		
NPC().print_description()