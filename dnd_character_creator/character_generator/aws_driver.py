#!/usr/local/bin/python3.6
from character_generator import Character, CharacterCreator
import pprint, json

def lambda_handler(json_input, context):
    creator = CharacterCreator(True, True, True, False)
    char = creator.char_generator()
    return(char.generate_dict())
