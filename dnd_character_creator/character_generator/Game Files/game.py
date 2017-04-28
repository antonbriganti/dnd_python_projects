from charcter import *
from character_generator import *

def print_menu():
    print('\nSelect:')
    print('1 - Fight')
    print('2 - Dodge')
    print('3 - Special')
    print('4 - Run')

def a_an(string):
    vowel = ['A','E','I','O','U','a','e','i','o','u']
    for char in vowel:
        if char == string[0]:
            return 'an ' + string
    return 'a ' + string


p_subrace, p_race, p_background, p_subclass, p_class, ability_score = optimised_rng_char()
print("You're " + a_an(p_background) + ' ' + p_subrace + ' ' + p_race)
print("Who is " + a_an(p_class))
print('With these stats!')
print('STR: ' + str(ability_score[0]))
print('DEX: ' + str(ability_score[1]))
print('CON: ' + str(ability_score[2]))
print('INT: ' + str(ability_score[3]))
print('WIS: ' + str(ability_score[4]))
print('CHA: ' + str(ability_score[5]))
player = Character('Player', p_race, p_subrace, p_class, p_subclass, ability_score)

print()

e_subrace, e_race, e_background, e_subclass, e_class, e_ability_score = optimised_rng_char()
print("Your enemy is " + a_an(e_background) + ' ' + e_subrace + ' ' + e_race)
print("Who is " + a_an(e_class))
print('With these stats!')
print('STR: ' + str(e_ability_score[0]))
print('DEX: ' + str(e_ability_score[1]))
print('CON: ' + str(e_ability_score[2]))
print('INT: ' + str(e_ability_score[3]))
print('WIS: ' + str(e_ability_score[4]))
print('CHA: ' + str(e_ability_score[5]))
enemy = Character('Enemy', e_race, e_subrace, e_class, e_subclass, e_ability_score)

gameflag = True
while gameflag:
    p_action = ''
    option = 0
    print()
    print()
    print("You're at " + str(player.health) +'hp!')
    print("They're at " + str(enemy.health)+'hp!')
    
    if player.health < 0:
        print('You have died')
        break

    if enemy.health < 0:
        print('You have won')
        break
    
    print_menu()
    
    try:
        option = int(input('What do you want to do? '))
    except ValueError:
        print("I don't know what you want, so I'll do nothing")

    print()

    if option == 1:
        p_action = 'Attack'
    elif option == 2:
        p_action = 'Dodge'
    elif option == 4:
        gameflag = False
        break

    e_action = enemy.enemy_choice()
    
    if e_action == 'Attack':
        print('The enemy goes to strike!')
        if p_action == 'Dodge':
            player.dodge(enemy.damage())
        else:
            print('The enemy lands their hit!')
            player.take_damage(enemy.damage())
            
        
    if p_action == 'Attack':
        if e_action == 'Dodge':
            print('The enemy goes to dodge!')
            enemy.dodge(player.damage())
        else:
            print('You land your hit!')
            enemy.take_damage(player.damage())

    if p_action == 'Dodge' and e_action == 'Dodge':
        print('You both go to dodge and feel quite silly')
            
        
