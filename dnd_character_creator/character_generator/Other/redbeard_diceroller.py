__author__ = 'AntonBriganti'
from ability_gen import *

'''
from: https://www.reddit.com/r/DnD/comments/4lgdyl/how_should_i_react_if_one_of_my_players_rolls_a/d3n3i6n

As a DM I allow my players to pick how they want to do stats.
The option I see most often chosen is one I affectionatley refer to as the Redbeard Matrix,
so named for the man who introduced me to it many years ago. Roll [4d6 drop the lowest die]
36 times filling a 6x6 grid starting in the top left corner and going across each row.
After you finish you pick the set of six you like best out of the grid, whether it is a
horizontal set, a vertical set, a diagonal set. It usually genterates ridiculous scores. E
veryone has fun and feel extrememly powerful at character creation.

'''

redbeard_matrix = []
for _ in range(6):
    redbeard_matrix.append(initial_abilities())

print("grid: ")
for line in redbeard_matrix:
    print(line)

print()
print("possible combinations \n")
for i in range(len(redbeard_matrix)):
    print('horizontal', i+1, redbeard_matrix[i])

print()
for j in range(len(redbeard_matrix)):
    vertical = []
    for k in range(len(redbeard_matrix)):
        vertical.append(redbeard_matrix[k][j])
    print('vertical', j+1, vertical)

print()
left_diagonal = []
for l in range(len(redbeard_matrix)):
    left_diagonal.append(redbeard_matrix[l][l])
print('top left diagonal', left_diagonal)

print()
right_diagonal = []
for m in range(len(redbeard_matrix)):
    right_diagonal.append(redbeard_matrix[m][len(redbeard_matrix)-m-1])
print('right left diagonal', right_diagonal)
