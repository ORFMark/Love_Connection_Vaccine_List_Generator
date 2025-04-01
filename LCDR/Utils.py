from datetime import datetime, timedelta

from LCDR.Excel.DataParser.TypeChecker import isValidChipCode


def stringifiedDate(datetimeToDisplay):
    if type(datetimeToDisplay) is datetime:
        return f"{datetimeToDisplay.month}/{datetimeToDisplay.day}/{datetimeToDisplay.year}"
    elif datetimeToDisplay is None:
        return ""
    else:
        raise TypeError(f"datetimeToDisplay must be datetime or None, was {type(datetimeToDisplay)}")


TODAY = datetime.now()
NEXT_WEEK = TODAY + timedelta(days=7)
LAST_WEEK = TODAY - timedelta(days=7)
LAST_45_DAYS = TODAY - timedelta(days=45)
NEXT_45_DAYS = TODAY + timedelta(days=45)
DATE_PATTERN_4_DIGIT_YEAR = "[0-9]+/[0-9]+/[0-9]{4}"
DATE_PATTERN_2_DIGIT_YEAR = "[0-9]+/[0-9]+/[0-9]{2}"


def stringifiedDateForFileName(datetimeToDisplay):
    return f"{datetimeToDisplay.month}_{datetimeToDisplay.day}_{datetimeToDisplay.year}"


def getDogCountsByFoster(listOfDogs):
    fosters = dict()
    for dog in listOfDogs:
        foster = dog.foster
        if fosters.get(foster):
            fosters[foster].append(dog)
        else:
            fosters[foster] = [dog]
    return fosters

def dateBetween(canidateDate, start, end):
    return canidateDate >= start and canidateDate <= end


def computeNeeds(dogList):
    neededBord = 0
    neededDHLPP = 0
    neededChips = 0
    for dog in dogList:
        dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
        dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
        if dogHasDHLPPDue:
            neededDHLPP += 1
        if dogHasBordetellaDue:
            neededBord += 1
        if not isValidChipCode(dog.chipCode):
            neededChips += 1
    return [neededDHLPP, neededBord, neededChips]

def sortListOfDogsInLocationOrder(listOfDogs):
    sortedListOfDogs = list()
    listOfVolunteers = list()
    for dog in listOfVolunteers:
        if(dog.vaccinePerson not in listOfVolunteers):
            listOfVolunteers.insert(len(listOfVolunteers), dog.vaccinePerson)
    listOfVolunteers.sort();
    for vaxVol in listOfVolunteers:
        for dog in listOfDogs:
            if(dog.vaccinePerson == vaxVol):
                sortedListOfDogs.insert(len(sortedListOfDogs), dog)
    return sortedListOfDogs


