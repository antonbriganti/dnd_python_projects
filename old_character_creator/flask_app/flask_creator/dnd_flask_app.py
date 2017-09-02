from character_generator_class_ver import *
from background_gen import *
from random import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/random')
def create_character():
    char = Character(True, True, False, False)
    char.char_generator()
    return render_template('random_character.html', character = char, backstory = backstory_creator())


if __name__ == '__main__':
    app.run()
