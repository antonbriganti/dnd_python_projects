#!/usr/local/bin/python3.6
import numpy
import json

class Table:
    def __init__(self):
        self.options = []
        self.probability_distribution = []
    
    def has_probability_distribution(self):
        return(len(self.probability_distribution))

def create_roll_table(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    
    roll_table = Table()
    
    for entry in data:
        roll_table.options.append(entry["option"])
        if "probability" in entry: roll_table.probability_distribution.append(entry["probability"])
        
    return roll_table

def roll_table(table_name):
    filename = "json/" + table_name + ".json"
    table = create_roll_table(filename)
    if table.has_probability_distribution():
        return numpy.random.choice(table.options, p=table.probability_distribution)
    else:
        return numpy.random.choice(table.options)
        
