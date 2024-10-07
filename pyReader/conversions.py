def convert_xp_to_level(xp):
    
    if xp >= 355000:
        return 20
    elif xp >= 305000:
        return 19
    elif xp >= 265000:
        return 18
    elif xp >= 225000:
        return 17
    elif xp >= 195000:
        return 16
    elif xp >= 165000:
        return 15
    elif xp >= 140000:
        return 14
    elif xp >= 120000:
        return 13
    elif xp >= 100000:
        return 12
    elif xp >= 85000:
        return 11
    elif xp >= 64000:
        return 10
    elif xp >= 48000:
        return 9
    elif xp >= 34000:
        return 8
    elif xp >= 23000:
        return 7
    elif xp >= 14000:
        return 6
    elif xp >= 6500:
        return 5
    elif xp >= 2700:
        return 4
    elif xp >= 900:
        return 3
    elif xp >= 300:
        return 2
    else:
        return 1