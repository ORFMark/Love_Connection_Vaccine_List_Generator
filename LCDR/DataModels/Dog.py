from datetime import datetime, timedelta

from LCDR.Excel.DataParser.TypeChecker import isValidChipCode
from LCDR.Utils import stringifiedDate, NEXT_WEEK


class Dog:

    def __init__(self):
        self.name =""
        self.gender =""
        self.foster =""
        self.chipCode =""
        self.ageInMonths =""
        self.vaccinePerson =""
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
    def __str__(self):
        return f"Name: {self.name}, Age (months): {self.ageInMonths}, Gender: {self.gender}"

    def getNextDueDHLPPVaccine(self):
        if len(self.DHLPPDates) == 0 and self.DHLPPComplete == 0:
            return None
        elif len(self.DHLPPDates) == 0:
            return TODAY
        elif self.DHLPPComplete >= len(self.DHLPPDates):
            return None
        elif len(self.DHLPPDates) > self.DHLPPComplete:
            if isinstance(self.DHLPPDates[self.DHLPPComplete], datetime):
                return self.DHLPPDates[self.DHLPPComplete]
            else:
                return None
        else:
            return TODAY

    def getNextDueBordetellaVaccine(self):
        if (len(self.BordetellaDates) == 0 and self.BordetellaComplete == 0) or self.BordetellaComplete >= len(
                self.BordetellaDates):
            return None
        elif len(self.BordetellaDates) == 0:
            return TODAY
        elif self.BordetellaComplete == len(self.BordetellaDates):
            return self.BordetellaDates[-1] + timedelta(days=365)
        elif len(self.BordetellaDates) > self.BordetellaComplete:
            if isinstance(self.BordetellaDates[self.BordetellaComplete], datetime):
                return self.BordetellaDates[self.BordetellaComplete]
            else:
                return None
        else:
            return TODAY


def generateDogInfoString(dog):
    dogInfoString = f"{dog.name}: "
    if dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK:
        dogInfoString += f"DHLPP #{dog.DHLPPComplete + 1} on {stringifiedDate(dog.getNextDueDHLPPVaccine())}, "
    if dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK:
        dogInfoString += f"Bordetella  on {stringifiedDate(dog.getNextDueBordetellaVaccine())}, "
    if not isValidChipCode(dog.chipCode):
        dogInfoString += "and a microchip."
    return dogInfoString


def printDogVaccineData(dog):
    print(f"DHLPP Dates: {dog.DHLPPDates}. Complete: {dog.DHLPPComplete}")
    print(f"Bord Dates: {dog.BordetellaDates}, Complete: {dog.BordetellaComplete}")
