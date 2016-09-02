'''
 ___  _____     Python - Encounter Generator - v 0.1
|    |_   _|
|   _  | |
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - December 2015
'''

from random import randint

def encounter(place):
    #PLACE == 1 --> URBAN
    if (place == 1):
        encounterArray = [line.strip() for line in open("./UrbanEncounters.dat", 'r',encoding='UTF-8')]
        dice = randint(0, len(encounterArray)-1)
        enemiesString = encounterArray[dice]
    else:
        enemiesString = 'We had a problem Sir'
    return enemiesString

#print encounter(1)
