#!/usr/local/bin/python3.6
from character_generator import Character, CharacterCreator
import pprint, json

def lambda_handler(json_input, context):
    creator = CharacterCreator(True, True, True, False)
    char = creator.char_generator()
    response = {'statusCode': 200,
                'headers': {
                            'Content-Type': 'application/json',
                            'Access-Control-Allow-Origin': '*'},
                'body': char.generate_json_string()
                }
    return response
