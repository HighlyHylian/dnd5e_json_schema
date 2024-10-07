import math, random, errors
import shlex
from re import search, IGNORECASE
from globalVariables import *
from errors import *
from conversions import convert_xp_to_level

def savingThrow(userInput, abilityScores):
# Does saving throw logic
    modifier = 0
    if not len(userInput) > 1:
        raise errors._myStFormatError()
    
    for value in userInput[1:]:
        match(value):
            case 'str' | "strenth":
                modifier += math.floor((abilityScores.get("str") - 10) / 2)
            case 'dex' | "dexterity":
                modifier += math.floor((abilityScores.get("dex") - 10) / 2)
            case 'con' | "constitution":
                modifier += math.floor((abilityScores.get("con") - 10) / 2)
            case 'int' | "intelligence":
                modifier += math.floor((abilityScores.get("int") - 10) / 2)
            case 'wis' | "wisdom":
                modifier += math.floor((abilityScores.get("wis") - 10) / 2)
            case 'cha' | "charisma":
                modifier += math.floor((abilityScores.get("cha") - 10) / 2)
            case _:
                raise errors._myStFormatError()
            
    rollValue = random.randint(1, 20)
    print(f"Modifier:\n{modifier}")
    print(f"Roll:\n{rollValue}")

def getRollInfo(userInput):
# Pulls from a tuple of strings to get the values of advantage (bool) and mod (int)
    advantage = 0
    mod = 0
    disadvantage = 0
    proficient = 0

    # Early exit for no arguments
    if len(userInput) <= 2:
        return [0, 0, 0, 0]

    for switch in userInput[2:]:
        if search("-a", switch):
            advantage = True
        if search("-m=[0-9]+", switch):
            mod = int(switch[3:])
        if search("-d", switch):
            disadvantage = True
        if search("-p=[0-9]+", switch):
            #switch[3:] will contain the proficiency bonus
            proficient = int(switch[3:])

    return proficient, disadvantage, advantage, mod

def castSpell(userInput, spells, xp):
    '''
    Casts spell from character sheet given a spell name
    Supported switches in regex format: 
    -l=[0-9]+" (cast at level [0-9]+) 
    -a (cast at advantage)
    -d (cast at disadvantage)"""
    -m=[0-9]+ (cast with modifier [0-9]+)
    '''
    userSpellName = userInput[1].replace("\"", "")
    found = False
    spell = {}
    level = 1
    diceCount = 0
    diceSides = 0
    for switch in userInput:
        if search("-l=[0-9]+", switch):
            level = int(switch[3:])
    for tempSpell in spells:
        if search(f".*{userSpellName}.*", tempSpell.get("name"), IGNORECASE):
            found = True
            spell = tempSpell

    if not found:
        raise _mySpellNotFound()
    

    print(spell.get("name"))
    levelDicePairs = spell.get("higher_level_dice")
    cantripLevelDicePairs = spell.get("cantrip_level_dice")

    # Get dice info
    damageDice = spell.get("damage_dice")
    diceCount, diceSides = validDice(damageDice)
    
    # This is a little ugly and should be fixed
    if levelDicePairs:
        for pair in levelDicePairs:
            if level >= pair[0]:
                diceCount, diceSides = validDice(pair[1])
    if cantripLevelDicePairs:
        for pair in cantripLevelDicePairs:
            if convert_xp_to_level(xp) >= pair[0]:
                diceCount, diceSides = validDice(pair[1])

        # TODO: Add switches to this roll. Also fix the fact that you must pass in the full line to 
        # roll() as if it was passed in via CLI. 
        # Eventually it should just take "dice {switch list}" instead of "r dice {switch list}"
    args = ['r', f"{diceCount}d{diceSides}"]
    if len(userInput) > 2:
        for arg in userInput[2:]:
            args.append(arg)
    print(roll(args))
        

# Rolling Main Function
def roll(userInput):
    proficient, disadvantage, advantage, mod = getRollInfo(userInput)
    count, sides = validDice(userInput[1])

    sum = 0
    print("Roll 1:")
    for i in range(count):
        roll = random.randint(1, sides)
        print(f"Die {i+1}: {roll}")
        sum += roll

    if advantage or disadvantage:
        print('-'*lw + "\nRoll 2")
        tempSum = 0
        for i in range(count):
            roll = random.randint(1, sides)
            print(f"Die {i+1}: {roll}")
            tempSum += roll
        print('-' * lw)
        if (advantage and tempSum > sum) or (disadvantage and tempSum < sum):
            print("Second roll wins")
            sum = tempSum
        else:
            print("First roll stays")
        print()

    return sum+mod+(math.floor((proficient + 1)/4))
        
# Returns dice info from string
def validDice(dice):
    try:
        if search("[0-9]+d[0-9]+", dice):
            dice = dice.split('d')
            return int(dice[0]), int(dice[1])
        else:
            raise (Exception)
    except:
        raise _myInvalidDice()