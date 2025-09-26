import traceback
from datetime import datetime, timedelta

from LCDR.Excel.DataParser.TypeChecker import isValidChipCode
from LCDR.Utils import stringifiedDate, vaccineDue


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
        self.rabiesAdminDate = ""
        self.rabiesVaccineDuration = 0
        self.lastRabisVaccineWas3Year = False;
        self.lastDAPPVaccineWas3Year = False;
    def __str__(self):
        return f"Name: {self.name}, Age (months): {self.ageInMonths}, Gender: {self.gender}, 5/1 complete: {self.DHLPPComplete}, 5/1 dates {self.DHLPPDates}, bord complete {self.BordetellaComplete}, bord dates {self.BordetellaDates}, chip {self.chipCode}"

    def getNextDueDHLPPVaccine(self):
        vaxDurationInDays = 365;
        if self.lastDAPPVaccineWas3Year:
            vaxDurationInDays = 365 *3
        if len(self.DHLPPDates) == 0 and self.DHLPPComplete == 0:
            return None
        elif len(self.DHLPPDates) == 0:
            return TODAY
        elif self.DHLPPComplete >= len(self.DHLPPDates):
            if type(self.DHLPPDates[-1]) is datetime:
                return self.DHLPPDates[-1] + timedelta(days=vaxDurationInDays)
            else:
                try:
                    return datetime.strptime(self.DHLPPDates[-1], "%m/%d/%y") + timedelta(days=vaxDurationInDays)
                except Exception as e:
                    print(e)
                    print(traceback.format_exc())
                    return self.DHLPPDates[-1]

        elif len(self.DHLPPDates) > self.DHLPPComplete:
            if isinstance(self.DHLPPDates[self.DHLPPComplete], datetime):
                return self.DHLPPDates[self.DHLPPComplete]
            else:
                return None
        else:
            return TODAY

    def getNextDueBordetellaVaccine(self):
        if (len(self.BordetellaDates) == 0 and self.BordetellaComplete == 0):
            return None
        elif len(self.BordetellaDates) == 0:
            return TODAY
        elif self.BordetellaComplete >= len(self.BordetellaDates):
            if type(self.BordetellaDates[-1]) is datetime:
                return self.BordetellaDates[-1] + timedelta(days=365)
            else:
                try:
                    return datetime.strptime(self.BordetellaDates[-1], "%m/%d/%y") + timedelta(days=365)
                except Exception as e:
                    print(e)
                    print(traceback.format_exc())
                    return self.BordetellaDates[-1]
        elif len(self.BordetellaDates) > self.BordetellaComplete:
            if isinstance(self.BordetellaDates[self.BordetellaComplete], datetime):
                return self.BordetellaDates[self.BordetellaComplete]
            else:
                return None
        else:
            return TODAY
    def getNextRabiesDate(self):
        try:
            return self.rabiesAdminDate + timedelta(days=self.rabiesVaccineDuration * 365)
        except:
            return None


def dogNeeds(dog):
    dogNeedsDLHPP = vaccineDue(dog.getNextDueDHLPPVaccine())
    dogNeedsMicroChip = not isValidChipCode(dog.chipCode)
    dogNeedsBordetella = vaccineDue(dog.getNextDueBordetellaVaccine)
    return [dogNeedsDLHPP, dogNeedsBordetella, dogNeedsMicroChip]
def generateDogInfoString(dog):
    dogInfoString = f"{dog.name}: "

    needs = dogNeeds(dog)
    dogNeedsDLHPP = needs[0]
    dogNeedsBordetella = needs[1]
    dogNeedsMicroChip = needs[2]

    if dog.getNextDueBordetellaVaccine() == dog.getNextDueDHLPPVaccine() and dogNeedsDLHPP and dogNeedsBordetella:
        dogInfoString += f"5 in 1 #{dog.DHLPPComplete + 1} and Bordetella #{dog.BordetellaComplete + 1} on {stringifiedDate(dog.getNextDueBordetellaVaccine())}"
        if dogNeedsMicroChip:
            dogInfoString += ", along with a microchip"
        else:
            dogInfoString += "."
    else:
        if dogNeedsDLHPP:
            dogInfoString += f"5 in 1 #{dog.DHLPPComplete + 1} on {stringifiedDate(dog.getNextDueDHLPPVaccine())}"
        if dogNeedsBordetella and dogNeedsMicroChip:
            dogInfoString += ", "
        elif dogNeedsDLHPP and dogNeedsBordetella:
            dogInfoString += " and "
        if dogNeedsBordetella:
            dogInfoString += f"Bordetella #{dog.BordetellaComplete + 1} on {stringifiedDate(dog.getNextDueBordetellaVaccine())}"
        if not dogNeedsMicroChip:
            dogInfoString += "."
        else:
            dogInfoString += " and a microchip."
    return dogInfoString


def printDogVaccineData(dog):
    print(f"{dog.name}")
    print(f"\tDHLPP Dates: {dog.DHLPPDates}. Complete: {dog.DHLPPComplete}")
    print(f"\tBord Dates: {dog.BordetellaDates}, Complete: {dog.BordetellaComplete}")
