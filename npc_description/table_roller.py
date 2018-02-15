#!/usr/local/bin/python3.6
import random
import json

def create_roll_table(filename):
    with open(filename) as data_file:
        roll_table = data_file.readlines()
    return roll_table

def roll_table(table_name):
    filename = table_name + ".txt"
    table = create_roll_table(filename)
    return random.choice(table).rstrip()
    
def generate_background():
    with open("backgrounds.json") as data_file:
        data = json.load(data_file)
    background = random.choice(data)
    return({"name":background["name"], "reason":random.choice(background["reasons"])})
