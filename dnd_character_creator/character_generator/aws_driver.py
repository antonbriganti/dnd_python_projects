from character_generator import Character
import pprint, json

def lambda_handler(json_input, context):
    char = Character(True, True, True, False)
    char.char_generator()
    return (char.generate_json())
