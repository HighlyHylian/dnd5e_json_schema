import math, random, errors

# Does saving throw logic
def savingThrow(userInput, abilityScores):
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