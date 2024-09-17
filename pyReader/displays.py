from globalVariables import lw


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


def displaySpells(spells):
    # Displays all spell info
    pass
