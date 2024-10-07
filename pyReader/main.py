import json
import random
import re
import shlex
import math
from rolling import *
from errors import *
from displays import *


# This was just to hide my user path. Should've thought about that earlier in the commit history. Whoops
file = open(r"pyReader\path.txt")
file_path = file.readline()
# print(file_path)


# Load JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract data from json file
name = data.get('name', str)
race = data.get('race', {})
classes = data.get('classes', [])
weapon_proficiencies = data.get('weapon_proficiencies', [])
armor_proficiencies = data.get('armor_proficiencies', [])
tool_proficiencies = data.get('tool_proficiencies', [])
ability_scores = data.get('ability_scores', [])
weapons = data.get('weapons', [])
equipment = data.get('equipment', [])
spells = data.get('spells', [])
xp = data.get('xp', int)

# Display name
print(name+'\'s sheet')

# Loop for cli
while (exit != True):
    userInput = shlex.split(input("> "), posix=False)
    print('-' * lw * 2)

    match userInput[0]:
        case 'e' | 'exit':
            break
        case 'd' | 'display':
            for value in userInput[1:]:
                match value:
                    case 'p' | 'proficiencies':
                        display_proficiencies(
                            weapon_proficiencies, armor_proficiencies, tool_proficiencies)
                    case 'e' | 'equipment':
                        display_equipment(equipment)
                    case 'r' | 'race':
                        display_race(race)
                    case 'c' | 'classes':
                        display_classes(classes, userInput)
                    case 'w' | 'weapons':
                        display_weapons(weapons)
                    case 's' | 'spells':
                        display_spells(userInput, spells)
                    case _:
                        pass
        case 'c' | 'cast':
            try:
                castSpell(userInput, spells, xp)
            except _mySpellNotFound as e:
                print(e)
            except:
                print("Error parsing spell")
        case 'r' | 'roll':
            # Flags + modifiers
            try:
                print(roll(userInput))
            except _myInvalidDice as e:
                print(e)
            except _myInvalidMod as e:
                print(e)
            except Exception as e:
                print("Error in parsing")
        case 's' | 'st' | 'saving':
            try:
                savingThrow(userInput, ability_scores)
            except Exception as e:
                print(e)
