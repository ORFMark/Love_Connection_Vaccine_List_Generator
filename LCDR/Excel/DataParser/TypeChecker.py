from datetime import datetime


def isValidChipCode(canidateCode):
    if canidateCode is None or canidateCode == ("Missing") or canidateCode == ('missing'):
        return False
    elif isinstance(canidateCode, datetime):
        return False
    elif isinstance(canidateCode, int):
        return True
    elif "E+" in canidateCode:
        return True
    else:
        return False
