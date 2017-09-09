#!/usr/local/bin/python3.6
from character_generator import Character, CharacterCreator
import pprint, json

def lambda_handler(json_input, context):
    if json_input["body"] == None: json_input["body"] = {"null":"body"}
    else: json_input["body"] = json.loads(json_input["body"])

    creator = CharacterCreator(True, True, True, json_input["body"])
    char = creator.char_generator()
    response = {'statusCode': 200,
                'headers': {
                            'Content-Type': 'application/json',
                            'Access-Control-Allow-Origin': '*'},
                'body': char.generate_json_string()
                }
    return response
