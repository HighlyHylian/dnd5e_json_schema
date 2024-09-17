__all__ = ['_myInvalidDice', '_myInvalidMod', '_mySpellNotFound', '_myStFormatError', '_mySpellDamageNotFound', '_myJSONFormatError']
class _myInvalidDice(Exception):
    def __init__(self, message=r'Invalid Dice Format. First argument must be in the format "{number}d{number}"'):
        super(_myInvalidDice, self).__init__(message)

class _myInvalidMod(Exception):
    def __init__(self, message=r'Invalid Mod Format. Mod must be in the format "-m={number}"'):
        super(_myInvalidMod, self).__init__(message)

class _mySpellNotFound(Exception):
    def __init__(self, message=r'Spell Not Found'):
        super(_mySpellNotFound, self).__init__(message)

class _myStFormatError(Exception):
    def __init__(self, message=r'Error with saving throw parsing. Must be in format "st {attribute} {advantage or disadvantage switches}"'):
        super(_myStFormatError, self).__init__(message)

class _mySpellDamageNotFound(Exception):
    def __init__(self, message=r'Error finding damage dice value. Ensure that they are in the JSON file'):
        super(_mySpellDamageNotFound, self).__init__(message)

class _myJSONFormatError(Exception):
    def __init__(self, message=r'Generic JSON file error. Check formatting of associated last CLI call'):
        super(_myJSONFormatError, self).__init__(message)