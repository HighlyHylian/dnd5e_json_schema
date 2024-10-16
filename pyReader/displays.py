from globalVariables import lw
from re import search, IGNORECASE, sub
from errors import *


def capitalizeWords(s):
  return sub(r'\w+', lambda m: m.group(0).capitalize(), s)


def display_weapons(weapons):
    # Display weapon details
    print("-" * (lw + 1) + "WEAPONS" + "-" * 22)
    for weapon in weapons:
        name = weapon.get('name', 'Unknown')

        # Damage
        damage_dice = weapon.get('damage', {}).get('dice', {})
        damage = f"{damage_dice.get('count', 1)}d{damage_dice.get('sides', 1)}"
        damage_type = weapon.get('damage', {}).get('type', 'None')

        # Range
        range_info = weapon.get('range', {})

        # Weight
        weight = weapon.get('weight', 'Unknown')

        # Equipped
        equipped = weapon.get('equipped', 'Unknown')

        print(f"Name: {name}")
        print(f"Damage: {damage}")
        print(f"Damage Type: {damage_type}")

        if range_info:
            range_short = range_info.get('short', 'None')
            range_long = range_info.get('long', 'None')
            range_display = f"Short: {range_short}, Long: {range_long}"
            print(f"Range: {range_display}")

        print(f"Weight: {weight}")
        print(f"Equipped: {equipped}")
        print("-" * lw * 2)
    print()


def display_classes(classes, userInput):
    # Displays class info
    # TODO: Add arguments (list what parts of the class)
    print("-" * (lw+2) + "CLASSES" + "-" * (lw+1))

    for c in classes:
        # Gather data
        subtype = c.get('subtype')
        hit_die = c.get('hit_die')
        spellcasting = c.get('spellcasting')
        features = c.get('features')
        source = c.get('source')  # TODO

        # Print data
        print(c.get('name'))
        print(f"Lvl. {c.get('level')}")
        if subtype:
            print(f"Subtype: {subtype}")
        if hit_die:
            print(f"Hit Die: {hit_die}")
        if spellcasting:
            print(f"Spellcasting ability: {spellcasting}")
        if features:
            print("-" * (lw+1) + "FEATURES" + "-" * (lw+1))
            for feature in features:
                # Gather data
                description = feature.get('description')
                source = feature.get('source')  # TODO
                print(feature.get('name'))
                if description:
                    print(description)
                print("." * 20)
            print()


def display_proficiencies(weapon_proficiencies, armor_proficiencies, tool_proficiencies):
    # Display proficiency info
    # TODO: Add arguments to choose weapon/armour/tool displays
    print("-" * (lw-5) + "WEAPON PROFICIENCIES" + "-" * (lw-5))
    for p in weapon_proficiencies:
        print(p)

    print("-" * (lw-5) + "ARMOR PROFICIENCIES" + "-" * (lw-4))
    for p in armor_proficiencies:
        print(p)

    print("-" * (lw-4) + "TOOL PROFICIENCIES" + "-" * (lw + -4))
    for p in tool_proficiencies:
        print(p)

    print("-" * 50 + '\n')


def display_race(race):
    # Display race info

    # Gather data
    subtype = race.get('subtype')
    size = race.get('size')
    traits = race.get('traits', [])
    actions = race.get('actions', [])
    senses = race.get('senses', {})  # TODO
    source = race.get('source', {})  # TODO.
    print("-" * (lw+3) + "RACE" + "-" * (lw+3))
    print("Race: ", race.get('name'))
    if subtype:
        print(f"Subtype: {subtype}")
    if size:
        print(f"Size: {size}")
    if traits:
        print("." * (lw-5) + "TRAITS" + "." * (lw-5))
        for trait in traits:
            name = trait.get('name')
            description = trait.get('description')
            source = trait.get('source', {})  # TODO
            if name:
                print(f"Name: {name}")
            if description:
                print(description)
            print("." * (lw-10))
        print()
    if actions:
        print("-" * (lw+2) + "ACTIONS" + "-" * (lw+1))
        # TODO
    if senses:
        print("-" * (lw+2) + "SENSES" + "-" * (lw+2))
        # TODO


def display_equipment(equipment):
    # Function to display equipment details
    print("-" * lw + "EQUIPMENT" + "-" * (lw+1))

    for item in equipment:
        # Gather data

        name = item.get('name', 'Unknown')
        weight = item.get('weight', {})
        description = item.get('description', {})
        magic = item.get('magic', {})
        source = item.get('source', 'Unknown')  # TODO
        quantity = item.get('quantity', {})

        # Print data
        print(f"Name: {name}")
        if weight:
            print(f"Weight: {weight}")
        if description:
            print(f"Description: {description}")
        if magic:
            print(f"Magic: {magic}")
        if quantity:
            print(f"Quantity: {quantity}")

        # Add other details here if needed
        print("." * lw)
    print()


def display_weapons(weapons):
    # Function to display weapon details
    print("-" * (lw + 1) + "WEAPONS" + "-" * 22)
    for weapon in weapons:
        name = weapon.get('name', 'Unknown')

        # Damage
        damage_dice = weapon.get('damage', {}).get('dice', {})
        damage = f"{damage_dice.get('count', 1)}d{damage_dice.get('sides', 1)}"
        damage_type = weapon.get('damage', {}).get('type', 'None')

        # Range
        range_info = weapon.get('range', {})

        # Weight
        weight = weapon.get('weight', 'Unknown')

        # Equipped
        equipped = weapon.get('equipped', 'Unknown')

        print(f"Name: {name}")
        print(f"Damage: {damage}")
        print(f"Damage Type: {damage_type}")

        if range_info:
            range_short = range_info.get('short', 'None')
            range_long = range_info.get('long', 'None')
            range_display = f"Short: {range_short}, Long: {range_long}"
            print(f"Range: {range_display}")

        print(f"Weight: {weight}")
        print(f"Equipped: {equipped}")
        print("-" * lw * 2)
    print()


def display_one_spell(spell):
    print(f"Name: {spell.get("name")}")
    print(f"Desc: {spell.get("description")}")
    optional_titles = {"higher_level", "material", "ritual",
                       "school", "attack_save", "damage_effect", "tags"}
    optionals = []
    for title in optional_titles:
        optionals.append([title, spell.get(title)])
    for optionalAttribute in optionals:
        if optionalAttribute[1]:
            print(f"{capitalizeWords(optionalAttribute[0])}: {optionalAttribute[1]}")

    # kind of unenecessary so I axed it. Feel free to restore
    # print(f"Level: {spell.get("level")}")
    print(f"Casting Time: {spell.get("casting_time")}")
    print(f"Range: {spell.get("range_area")}")
    print(f"Components: {spell.get("components")}")
    print(f"Duration: {spell.get("duration")}")


def display_spells(userInput, spells):
    # Display spells or specific spell

    # If searching for a specific spell, search
    # If spell not found, raise exception
    if len(userInput) > 2:
        userSpellName = userInput[2].replace("\"", "")
        for tempSpell in spells:
            if search(f".*{userSpellName}.*", tempSpell.get("name"), IGNORECASE):
                display_one_spell(tempSpell)
                return
        raise _mySpellNotFound()

    # Displays all spell info
    for spell in spells:
        print(f"Name: {spell.get("name")}")
        print(f"Desc: {spell.get("description")}")
        # kind of unenecessary so I axed it. Feel free to restore
        # print(f"Level: {spell.get("level")}")
        print(f"Casting Time: {spell.get("casting_time")}")
        print(f"")
