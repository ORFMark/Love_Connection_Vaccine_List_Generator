import openpyxl
from enum import Enum
import csv
from datetime import datetime
from datetime import timedelta
import openpyxl
import re


class DogSpreadsheetSheet(Enum):
    ADOPTABLE = 0
    ADOPTED = 1


class AdoptableColums(Enum):
    FOLDER = 0
    NAME = 1
    GENDER = 2
    BIRTHDAY = 3
    AGE_IN_MONTHS = 4
    INTAKE_DATE = 5
    CHIP_CODE = 6
    COLOR = 7
    SIZE = 8
    BREED = 9
    LITTER = 10
    FOSTER = 11
    ALTER_DATE = 12
    RABIES_DATE = 13
    FECAL = 14
    SNAP = 15
    MED_NOTES = 16
    VACCINE_PERSON = 17
    DHLPP_1 = 18
    DHLPP_2 = 19
    DHLPP_3 = 20
    DHLPP_4 = 21
    DHLPP_5 = 22
    Bordetella_1 = 23
    Bordetella_2 = 24
    VACCINES_DUE_LOOP = 25
    PICTURE_IN_BIO = 26
    ALTER_DONE = 27
    AQUISITION_METHOD = 28
    GOOD_WITH_DOGS = 29
    GOOD_WITH_CATS = 30
    GOOD_WITH_KIDS = 31
    BEHAVIOR_NOTES = 32


class AdoptedColums(Enum):
    RECORDS = 0;
    LCDR_NAME = 1
    GENDER = 2;
    DOB = 3
    AGE_IN_MONTHS = 4
    INTAKE = 5
    MICROCHIP = 6
    COLOR = 7
    SIZE = 8
    BREED = 9
    LITTER = 10
    FOSTER = 11
    ALTER_DATE = 12
    RABIES_DATE = 13
    FECAL = 14
    SNAP = 15
    MED_NOTES = 16
    VACCINE_PERSON = 17
    DHLPP_1 = 18
    DHLPP_2 = 19
    DHLPP_3 = 20
    DHLPP_4 = 21
    DHLPP_5 = 22
    Bordetella_1 = 23
    Bordetella_2 = 24
    ADOPTED_NAME = 25
    ADOPTED_FAMILY = 26
    ADOPTED_FAMILY_CONTACT = 27
    ADOPTED_DATE = 28
    PAYMENT_COLLECTED = 29
    CONTRACT_COMPLETE = 30
    FOLLOWUP = 31
    NOTES = 32


INFO_ROW = 1
HEADER_ROW = 2

TODAY = datetime.now()
NEXT_WEEK = TODAY + timedelta(days=7)
LAST_WEEK = TODAY - timedelta(days=7)

DATE_PATTERN_4_DIGIT_YEAR = "[0-9]+/[0-9]+/[0-9]{4}"
DATE_PATTERN_2_DIGIT_YEAR = "[0-9]+/[0-9]+/[0-9]{2}"


class CellColor(Enum):
    YELLOW = "FFFFFF00";
    RED = "FFFF0000";
    BRIGHT_GREEN = "FF00FF00";


def getCellColor(cell):
    return cell.fill.fgColor.index


def countColoredCells(cellColorCode, listOfCells):
    numOfColoredCells = 0;
    for cell in listOfCells:
        if getCellColor(cell) == cellColorCode:
            numOfColoredCells += 1
    return numOfColoredCells


def doesCellCount(excelRow, index):
    cell = excelRow[index]
    if getCellColor(cell) == CellColor.YELLOW.value or getCellColor(cell) == CellColor.RED.value:
        return False
    elif cell.value != "N/A" and cell.value != None and cell.value != "n/A":
        return True


class AdoptableDogRecord:
    def __init__(self, excelRow):
        self.name = excelRow[AdoptableColums.NAME.value].value
        self.gender = excelRow[AdoptableColums.GENDER.value].value
        self.foster = excelRow[AdoptableColums.FOSTER.value].value
        self.chipCode = excelRow[AdoptableColums.CHIP_CODE.value].value
        self.ageInMonths = excelRow[AdoptableColums.AGE_IN_MONTHS.value].value
        self.vaccinePerson = excelRow[AdoptableColums.VACCINE_PERSON.value].value
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_1.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_1.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_2.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_2.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_3.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_3.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_4.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_4.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_5.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_5.value):
            self.DHLPPComplete += 1
        self.BordetellaDates.append(excelRow[AdoptableColums.Bordetella_1.value].value)
        if doesCellCount(excelRow, AdoptableColums.Bordetella_1.value):
            self.BordetellaComplete += 1
        self.BordetellaDates.append(excelRow[AdoptableColums.Bordetella_2.value].value)
        if doesCellCount(excelRow, AdoptableColums.Bordetella_2.value):
            self.BordetellaComplete += 1
        while ("N/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while ("N/a" in self.BordetellaDates):
            self.BordetellaDates.remove("N/a")
        while ("" in self.BordetellaDates):
            self.BordetellaDates.remove("")
        while ("Missing" in self.BordetellaDates):
            self.BordetellaDates.remove("Missing")
        while ("N/A" in self.DHLPPDates):
            self.DHLPPDates.remove("N/A")
        while ("N/a" in self.DHLPPDates):
            self.DHLPPDates.remove("N/a")
        while ("Missing" in self.DHLPPDates):
            self.DHLPPDates.remove("Missing")
        while ("" in self.DHLPPDates):
            self.DHLPPDates.remove("")
        for i in range(0, len(self.DHLPPDates)):
            if isinstance(self.DHLPPDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.DHLPPDates[i])
                if (result):
                    self.DHLPPDates[i] = datetime.strptime(result[0], "%m/%d/%Y")
        for i in range(0, len(self.BordetellaDates)):
            if isinstance(self.BordetellaDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.BordetellaDates[i])
                if (result):
                    self.BordetellaDates[i] = datetime.strptime(result[0], "%m/%d/%Y")

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


class AdoptedDogRecord:
    def __init__(self, excelRow):
        self.name = excelRow[AdoptedColums.LCDR_NAME.value].value
        self.gender = excelRow[AdoptedColums.GENDER.value].value
        self.foster = excelRow[AdoptedColums.FOSTER.value].value
        self.chipCode = excelRow[AdoptedColums.MICROCHIP.value].value
        self.ageInMonths = excelRow[AdoptedColums.AGE_IN_MONTHS.value].value
        self.vaccinePerson = excelRow[AdoptedColums.VACCINE_PERSON.value].value
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_1.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_1.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_2.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_2.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_3.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_3.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_4.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_4.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_5.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_5.value):
            self.DHLPPComplete += 1
        self.BordetellaDates.append(excelRow[AdoptedColums.Bordetella_1.value].value)
        if doesCellCount(excelRow, AdoptedColums.Bordetella_1.value):
            self.BordetellaComplete += 1
        self.BordetellaDates.append(excelRow[AdoptedColums.Bordetella_2.value].value)
        if doesCellCount(excelRow, AdoptedColums.Bordetella_2.value):
            self.BordetellaComplete += 1
        while ("N/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while ("n/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while ("N/a" in self.BordetellaDates):
            self.BordetellaDates.remove("N/a")
        while ("" in self.BordetellaDates):
            self.BordetellaDates.remove("")
        while ("Missing" in self.BordetellaDates):
            self.BordetellaDates.remove("Missing")
        while ("N/A" in self.DHLPPDates):
            self.DHLPPDates.remove("N/A")
        while ("N/a" in self.DHLPPDates):
            self.DHLPPDates.remove("N/a")
        while ("n/A" in self.DHLPPDates):
            self.DHLPPDates.remove("n/A")
        while ("Missing" in self.DHLPPDates):
            self.DHLPPDates.remove("Missing")
        while ("" in self.DHLPPDates):
            self.DHLPPDates.remove("")
        for i in range(0, len(self.DHLPPDates)):
            if isinstance(self.DHLPPDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.DHLPPDates[i])
                if (result):
                    self.DHLPPDates[i] = datetime.strptime(result[0], "%m/%d/%Y")
                else:
                    result = re.search(DATE_PATTERN_2_DIGIT_YEAR, self.DHLPPDates[i])
                    if (result):
                        self.DHLPPDates[i] = datetime.strptime(result[0], "%m/%d/%y")
        for i in range(0, len(self.BordetellaDates)):
            if isinstance(self.BordetellaDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.BordetellaDates[i])
                if (result):
                    self.BordetellaDates[i] = datetime.strptime(result[0], "%m/%d/%Y")

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
            return self.DHLPPDates[self.DHLPPComplete]
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
            return self.BordetellaDates[self.BordetellaComplete]
        else:
            return TODAY


def stringifiedDate(datetimeToDisplay):
    return f"{datetimeToDisplay.month}/{datetimeToDisplay.day}/{datetimeToDisplay.year}"


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


def generateDogInfoString(dog):
    dogInfoString = f"{dog.name}: "
    if dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK:
        dogInfoString += f"DHLPP #{dog.DHLPPComplete + 1} on {stringifiedDate(dog.getNextDueDHLPPVaccine())}, "
    if dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK:
        dogInfoString += f"Bordetella  on {stringifiedDate(dog.getNextDueBordetellaVaccine())}, "
    if not isValidChipCode(dog.chipCode):
        dogInfoString += "and a microchip."
    return dogInfoString


def getDogCountsByFoster(adoptableDogsNeedingVaccines):
    fostersToNotify = dict()
    for dog in adoptableDogsNeedingVaccines:
        foster = dog.foster
        if fostersToNotify.get(foster):
            fostersToNotify[foster].append(dog)
        else:
            fostersToNotify[foster] = [dog]
    fosters = fostersToNotify.keys();
    for foster in fosters:
        print(f"{foster} has {len(fostersToNotify[foster])}")


def generateMessagesInShell(adoptableDogsNeedingVaccines):
    fostersToNotify = dict()
    for dog in adoptableDogsNeedingVaccines:
        foster = dog.foster
        if fostersToNotify.get(foster):
            fostersToNotify[foster].append(dog)
        else:
            fostersToNotify[foster] = [dog]
    fosters = fostersToNotify.keys();
    for foster in fosters:
        print(f"\n\nHi {foster},\nYour foster(s) have the following vaccines due in the next week: \n ")
        for dog in fostersToNotify[foster]:
            print(generateDogInfoString(dog))
        if fostersToNotify[foster][0].vaccinePerson != "":
            print(
                f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.")
        else:
            print(
                f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.")
        print("Thank you!\nThe LCDR Team\n\n")

    print("This completes the vaccines for the week, good job!")


def generateMessagesInShellAdopted(adoptableDogsNeedingVaccines):
    for dog in adoptableDogsNeedingVaccines:
        print(f"\n\nYour Pup has the following vaccines due in the next week: \n ")
        print(generateDogInfoString(dog))
        if dog.vaccinePerson != "":
            print(
                f"\nYour vaccine volunteer is {dog.vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.")
        else:
            print(
                f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.")
        print("Thank you!\nThe LCDR Team\n\n")

    print("This completes the vaccines for the week, good job!")


def generateVaccinePersonReport(adoptableDogsNeedingVaccines):
    vaccinePeople = dict()
    print("VaxPerson | min # chats | DHLPP | Bord | chips")
    for dog in adoptableDogsNeedingVaccines:
        vaccinePerson = "Unknown"
        if dog.vaccinePerson and dog.vaccinePerson != '':
            canidatePerson = dog.vaccinePerson;
            canidatePerson = canidatePerson.strip()
            canidatePerson = canidatePerson.lower()
            canidatePerson = canidatePerson[0].upper() + canidatePerson[1:]
            vaccinePerson = canidatePerson
        if vaccinePeople.get(vaccinePerson):
            vaccinePeople[vaccinePerson].append(dog)
        else:
            vaccinePeople[vaccinePerson] = [dog]
    sortedKeys = list(vaccinePeople.keys())
    sortedKeys.sort()
    for person in sortedKeys:
        neededBoard = 0;
        neededDHLPP = 0;
        neededChips = 0;
        fosters = set();
        for dog in vaccinePeople[person]:
            fosters.add(dog.foster)
            dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
            dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
            if dogHasDHLPPDue:
                neededDHLPP += 1
            if dogHasBordetellaDue:
                neededBoard += 1
            if not isValidChipCode(dog.chipCode):
                neededChips += 1

        print("%s | %s | %s | %s | %s" % (
        person.center(9, ' '), str(len(fosters)).center(11, ' '), str(neededDHLPP).center(5, ' '),
        str(neededBoard).center(4, " "), str(neededChips).center(5, " ")))


def exportMessagesToCSV(adoptableDogsNeedingVaccines):
    fostersToNotify = dict()
    for dog in adoptableDogsNeedingVaccines:
        foster = dog.foster
        if fostersToNotify.get(foster):
            fostersToNotify[foster].append(dog)
        else:
            fostersToNotify[foster] = [dog]
    fosters = fostersToNotify.keys();
    with open("Output/messages.txt", "w", newline='') as csvFile:
        messageWriter = csv.writer(csvFile, delimiter='\n', quotechar="\t")
        for foster in fosters:
            messageString = "";
            messageString += (f"\n\nHi {foster},\nYour foster(s) have the following vaccines due in the next week: \n ")
            for dog in fostersToNotify[foster]:
                messageString += (generateDogInfoString(dog)) + "\n"
            if fostersToNotify[foster][0].vaccinePerson != "":
                messageString += (
                    f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.")
            else:
                messageString += (
                    f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.")
            messageString += ("Thank you!\nThe LCDR Team\n\n")
            messageWriter.writerow([foster, messageString])


def stringifiedDateForFileName(datetimeToDisplay):
    return f"{datetimeToDisplay.month}_{datetimeToDisplay.day}_{datetimeToDisplay.year}"


def exportAdoptableDogMessagesToFile(adoptableDogsNeedingVaccines):
    filename = f"Adoptable_Dog_messages_{stringifiedDateForFileName(TODAY)}.txt"
    fostersToNotify = dict()
    for dog in adoptableDogsNeedingVaccines:
        foster = dog.foster
        if fostersToNotify.get(foster):
            fostersToNotify[foster].append(dog)
        else:
            fostersToNotify[foster] = [dog]
    fosters = fostersToNotify.keys();
    with open(filename, "w") as f:
        f.write(
            "Your vaccine volunteer is {vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n\n")
        f.write(
            "We don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n\n")
        f.write("There is an event this week on {DATE} at {PLACE}, you can bring your dog there for vaccines\n\n")
        for dog in adoptableDogsNeedingVaccines:
            f.write(generateDogInfoString(dog) + "\n")
        f.write("\n\n")
        for foster in fosters:
            f.write(f"\n\nHi {foster},\nYour foster(s) have the following vaccines due in the next week: \n ")
            for dog in fostersToNotify[foster]:
                f.write(generateDogInfoString(dog))
                f.write("\n")
            if fostersToNotify[foster][0].vaccinePerson and fostersToNotify[foster][0].vaccinePerson != "":
                f.write(
                    f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n")
            else:
                f.write(
                    f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n")
            f.write("Thank you!\nThe LCDR Team\n\n")

        f.write("This completes the vaccines for the week, good job!")


def exportAdoptedDogMessagesToFile(adoptableDogsNeedingVaccines):
    filename = f"Adopted_Dog_messages_{stringifiedDateForFileName(TODAY)}.txt"
    fostersToNotify = dict()

    with open(filename, "w") as f:
        f.write(
            "Your vaccine volunteer is {vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n\n")
        f.write(
            "We don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n\n")
        f.write("There is an event this week on {DATE} at {PLACE}, you can bring your dog there for vaccines\n\n")
        for dog in adoptableDogsNeedingVaccines:
            f.write(generateDogInfoString(dog) + "\n")
        f.write("\n\n")
        for dog in adoptableDogsNeedingVaccines:
            f.write(f"\n\nYour Pup has the following vaccines due in the next week: \n ")
            f.write(generateDogInfoString(dog))
            if dog.vaccinePerson and dog.vaccinePerson != "":
                f.write(
                    f"\n\nYour vaccine volunteer is {dog.vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n")
            else:
                f.write(
                    f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n")
            f.write("Thank you!\nThe LCDR Team\n\n")

        f.write("This completes the vaccines for the week, good job!")


def writeEventListToFile(dogsToWrite):
    filename = f"EventFile_{stringifiedDateForFileName(TODAY)}.csv"
    with open(filename, "w", newline='\n') as eventFile:
        eventWriter = csv.writer(eventFile)
        eventWriter.writerow(["Dog Name", "Vaccine Volunteer", "Chip", "DHLPP", "Bord"])
        for dog in dogsToWrite:
            nextDueDHLPP = dog.getNextDueDHLPPVaccine()
            if (nextDueDHLPP != None and nextDueDHLPP <= NEXT_WEEK):
                nextDueDHLPP = stringifiedDateForFileName(nextDueDHLPP);
            else:
                nextDueDHLPP = ""
            nextDueBord = dog.getNextDueBordetellaVaccine()
            if nextDueBord != None and nextDueBord <= NEXT_WEEK:
                nextDueBord = stringifiedDateForFileName(nextDueBord)
            else:
                nextDueBord = ""
            chipCode = ""
            if not isValidChipCode(dog.chipCode):
                try:
                    chipCode = stringifiedDateForFileName(dog.chipCode)
                except:
                    chipCode = dog.chipCode
            eventWriter.writerow([dog.name, dog.vaccinePerson, chipCode, nextDueDHLPP, nextDueBord])


def printDogVaccineData(dog):
    print(f"DHLPP Dates: {dog.DHLPPDates}. Complete: {dog.DHLPPComplete}")
    print(f"Bord Dates: {dog.BordetellaDates}, Complete: {dog.BordetellaComplete}")


PATH_TO_FILE = "Data Files/LCDR_Dog_Sheet_07_11_2024.xlsx"
wb = openpyxl.load_workbook(PATH_TO_FILE, data_only=True)
ws = wb.worksheets[0]
rowNum = 0
redCell = ws.cell(1, 26)
print(f"FG: {redCell.fill.fgColor.index}")
adoptableDogsWithNeeds = []
adoptedDogsWithNeeds = []
allDogsWithNeeds = []
for row in ws:
    rowNum += 1
    if rowNum == HEADER_ROW or rowNum == INFO_ROW:
        continue
    dog = AdoptableDogRecord(row)
    if getCellColor(row[AdoptableColums.VACCINE_PERSON.value]) == CellColor.BRIGHT_GREEN.value:
        continue
    dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
    dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
    if dogHasDHLPPDue or dogHasBordetellaDue:
        adoptableDogsWithNeeds.append(dog)
    if (dog.name == None):
        break
print(f"There are {len(adoptableDogsWithNeeds)} that need a vaccine")
ws = wb.worksheets[1]
rowNum = 0
for row in ws:
    rowNum += 1
    if rowNum == HEADER_ROW or rowNum == INFO_ROW:
        continue
    dog = AdoptedDogRecord(row)
    if getCellColor(row[AdoptableColums.VACCINE_PERSON.value]) == CellColor.BRIGHT_GREEN.value:
        continue
    dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
    dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
    if dogHasDHLPPDue or dogHasBordetellaDue:
        adoptedDogsWithNeeds.append(dog)
    if dog.name == None:
        break
print(f"There are {len(adoptedDogsWithNeeds)} that need a vaccine")
allDogsWithNeeds = adoptableDogsWithNeeds + adoptedDogsWithNeeds

print("Adoptable: ")
for dog in adoptableDogsWithNeeds:
    print(generateDogInfoString(dog))
print()
print("Adopted: ")
for dog in adoptedDogsWithNeeds:
    print(generateDogInfoString(dog))
print()
generateVaccinePersonReport(allDogsWithNeeds)
exportAdoptableDogMessagesToFile(adoptableDogsWithNeeds)
exportAdoptedDogMessagesToFile(adoptedDogsWithNeeds)
writeEventListToFile(allDogsWithNeeds)
