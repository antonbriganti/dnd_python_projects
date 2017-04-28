from random import *


names = []

with open('human_names.txt') as file:
    for line in file:
        names.append(line.split(','))

male_names = names[0]
female_names = names[1]
last_names = names[2]

gender = randint(0,1)
if gender == 0:
    fname = male_names[randint(0,len(male_names))]
else:
    fname = female_names[randint(0,len(female_names))]
lname = last_names[randint(0, len(last_names))]

print(fname, lname)