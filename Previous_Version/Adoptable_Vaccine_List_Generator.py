from enum import Enum
import csv
from datetime import datetime
from datetime import timedelta
import openpyxl

class AdoptableColums(Enum):
    FOLDER        = 0
    NAME          = 1
    GENDER        = 2
    BIRTHDAY      = 3
    AGE_IN_MONTHS = 4
    INTAKE_DATE   = 5 
    CHIP_CODE     = 6
    COLOR         = 7
    SIZE          = 8
    BREED         = 9
    LITTER        = 10
    FOSTER        = 11
    ALTER_DATE    = 12
    RABIES_DATE   = 13
    FECAL         = 14
    SNAP          = 15
    MED_NOTES     = 16
    VACCINE_PERSON = 17
    COMPLETE_DHLPP = 18
    DHLPP_1       = 19
    DHLPP_2       = 20
    DHLPP_3       = 21
    DHLPP_4       = 22
    DHLPP_5       = 23
    COMPLETE_Bordetella = 24
    Bordetella_1 = 25
    Bordetella_2 = 26
    VACCINES_DUE_LOOP = 27
    PICTURE_IN_BIO = 28
    ALTER_DONE    = 29
    AQUISITION_METHOD = 30
    GOOD_WITH_DOGS = 31
    GOOD_WITH_CATS = 32
    GOOD_WITH_KIDS = 33
    BEHAVIOR_NOTES = 34
    
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
    DHLPP_COMPLETE = 18
    DHLPP_1       = 19
    DHLPP_2       = 20
    DHLPP_3       = 21
    DHLPP_4       = 22
    DHLPP_5       = 23
    COMPLETE_Bordetella = 24
    Bordetella_1 = 25
    Bordetella_2 = 26
    ADOPTED_NAME = 28
    ADOPTED_FAMILY = 29
    ADOPTED_FAMILY_CONTACT = 30
    ADOPTED_DATE = 31
    PAYMENT_COLLECTED = 32
    CONTRACT_COMPLETE =33
    FOLLOWUP = 34
    NOTES = 35
INFO_ROW = 0
HEADER_ROW = 1

TODAY = datetime.now()
NEXT_WEEK =TODAY + timedelta(days = 7)
LAST_WEEK = TODAY - timedelta(days = 7)

class AdoptableDogRecord:
    def __init__(self, csvRow):
        self.folderHolder = csvRow[AdoptableColums.FOLDER.value]
        self.name = csvRow[AdoptableColums.NAME.value]
        self.gender = csvRow[AdoptableColums.GENDER.value]
        self.birthday = csvRow[AdoptableColums.BIRTHDAY.value]
        self.ageInMonths = csvRow[AdoptableColums.AGE_IN_MONTHS.value]
        self.chipCode = csvRow[AdoptableColums.CHIP_CODE.value]
        self.color = csvRow[AdoptableColums.COLOR.value]
        self.size = csvRow[AdoptableColums.SIZE.value]
        self.breed = csvRow[AdoptableColums.BREED.value]
        self.litter = csvRow[AdoptableColums.LITTER.value]
        self.foster = csvRow[AdoptableColums.FOSTER.value]
        self.alterDate = csvRow[AdoptableColums.ALTER_DATE.value]
        self.rabiesDate = csvRow[AdoptableColums.RABIES_DATE.value]
        self.fecalDate = csvRow[AdoptableColums.FECAL.value]
        self.snapDate = csvRow[AdoptableColums.SNAP.value]
        self.medicalNotes = csvRow[AdoptableColums.MED_NOTES.value]
        self.vaccinePerson = csvRow[AdoptableColums.VACCINE_PERSON.value]
        self.DHLPPComplete = int(csvRow[AdoptableColums.COMPLETE_DHLPP.value])
        self.DHLPPDates = [csvRow[AdoptableColums.DHLPP_1.value],csvRow[AdoptableColums.DHLPP_2.value],csvRow[AdoptableColums.DHLPP_3.value],csvRow[AdoptableColums.DHLPP_4.value],csvRow[AdoptableColums.DHLPP_5.value]]
        self.BordetellaDates = [csvRow[AdoptableColums.Bordetella_1.value], csvRow[AdoptableColums.Bordetella_2.value]]
        self.BordetellaComplete = int(csvRow[AdoptableColums.COMPLETE_Bordetella.value])
        self.otherVaccinesDue = csvRow[AdoptableColums.VACCINES_DUE_LOOP.value]           
        self.picturePresent = bool(csvRow[AdoptableColums.PICTURE_IN_BIO.value])
        self.alterDone = bool(csvRow[AdoptableColums.ALTER_DONE.value])
        self.aquistionMethod = csvRow[AdoptableColums.AQUISITION_METHOD.value]
        self.goodWithDogs = csvRow[AdoptableColums.GOOD_WITH_DOGS.value]
        self.goodWithCats = csvRow[AdoptableColums.GOOD_WITH_CATS.value]
        self.goodWithKids = csvRow[AdoptableColums.GOOD_WITH_KIDS.value]
        self.behaviorNotes = csvRow[AdoptableColums.BEHAVIOR_NOTES.value]
        while("N/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while("N/a" in self.BordetellaDates):
            self.BordetellaDates.remove("N/a")
        while("" in self.BordetellaDates):
            self.BordetellaDates.remove("")
        while("Missing" in self.BordetellaDates):
            self.BordetellaDates.remove("Missing")
        while("N/A" in self.DHLPPDates):
            self.DHLPPDates.remove("N/A")
        while("N/a" in self.DHLPPDates):
            self.DHLPPDates.remove("N/a")
        while("Missing" in self.DHLPPDates):
            self.DHLPPDates.remove("Missing")
        while("" in self.DHLPPDates):
            self.DHLPPDates.remove("")
            
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
            return datetime.strptime(self.DHLPPDates[self.DHLPPComplete], '%m/%d/%Y')
        else:
            return TODAY 
    def getNextDueBordetellaVaccine(self):
        if (len(self.BordetellaDates) == 0 and self.BordetellaComplete == 0) or self.BordetellaComplete >=  len(self.BordetellaDates):
            return None
        elif len(self.BordetellaDates) == 0:
            return TODAY
        elif self.BordetellaComplete >= len(self.BordetellaDates):
            return None
        elif len(self.BordetellaDates) > self.BordetellaComplete:
            return datetime.strptime(self.BordetellaDates[self.BordetellaComplete], '%m/%d/%Y')
        else:
            return TODAY 
class AdoptedDogRecord:
    def __init__(self, csvRow):
        self.folderHolder = csvRow[AdoptedColums.RECORDS.value]
        self.name = csvRow[AdoptedColums.LCDR_NAME.value]
        self.gender = csvRow[AdoptedColums.GENDER.value]
        self.birthday = csvRow[AdoptedColums.DOB.value]
        self.ageInMonths = csvRow[AdoptedColums.AGE_IN_MONTHS.value]
        self.chipCode = csvRow[AdoptedColums.MICROCHIP.value]
        self.color = csvRow[AdoptedColums.COLOR.value]
        self.size = csvRow[AdoptedColums.SIZE.value]
        self.breed = csvRow[AdoptedColums.BREED.value]
        self.litter = csvRow[AdoptedColums.LITTER.value]
        self.foster = csvRow[AdoptedColums.FOSTER.value]
        self.alterDate = csvRow[AdoptedColums.ALTER_DATE.value]
        self.rabiesDate = csvRow[AdoptedColums.RABIES_DATE.value]
        self.fecalDate = csvRow[AdoptedColums.FECAL.value]
        self.snapDate = csvRow[AdoptedColums.SNAP.value]
        self.medicalNotes = csvRow[AdoptedColums.MED_NOTES.value]
        self.vaccinePerson = csvRow[AdoptedColums.VACCINE_PERSON.value]
        self.DHLPPComplete = int(csvRow[AdoptedColums.DHLPP_COMPLETE.value])
        self.DHLPPDates = [csvRow[AdoptedColums.DHLPP_1.value],csvRow[AdoptedColums.DHLPP_2.value],csvRow[AdoptedColums.DHLPP_3.value],csvRow[AdoptedColums.DHLPP_4.value],csvRow[AdoptedColums.DHLPP_5.value]]
        self.BordetellaDates = [csvRow[AdoptedColums.Bordetella_1.value], csvRow[AdoptedColums.Bordetella_2.value]]
        self.BordetellaComplete = int(csvRow[AdoptedColums.COMPLETE_Bordetella.value])
        while("N/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while("N/a" in self.BordetellaDates):
            self.BordetellaDates.remove("N/a")
        while("" in self.BordetellaDates):
            self.BordetellaDates.remove("")
        while("Missing" in self.BordetellaDates):
            self.BordetellaDates.remove("Missing")
        while("N/A" in self.DHLPPDates):
            self.DHLPPDates.remove("N/A")
        while("N/a" in self.DHLPPDates):
            self.DHLPPDates.remove("N/a")
        while("Missing" in self.DHLPPDates):
            self.DHLPPDates.remove("Missing")
        while("" in self.DHLPPDates):
            self.DHLPPDates.remove("")
        
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
            return datetime.strptime(self.DHLPPDates[self.DHLPPComplete], '%m/%d/%Y')
        else:
            return TODAY 
    def getNextDueBordetellaVaccine(self):
        if (len(self.BordetellaDates) == 0 and self.BordetellaComplete == 0) or self.BordetellaComplete >=  len(self.BordetellaDates):
            return None
        elif len(self.BordetellaDates) == 0:
            return TODAY
        elif self.BordetellaComplete >= len(self.BordetellaDates):
            return None
        elif len(self.BordetellaDates) > self.BordetellaComplete:
            return datetime.strptime(self.BordetellaDates[self.BordetellaComplete], '%m/%d/%Y')
        else:
            return TODAY 
        
def stringifiedDate(datetimeToDisplay):
    return f"{datetimeToDisplay.month}/{datetimeToDisplay.day}/{datetimeToDisplay.year}"
def isValidChipCode(canidateCode):
    if canidateCode == ("Missing") or canidateCode == ('missing'):
        return False
    else:
        try:
            datetime.strptime(canidateCode, '%m/%d/%Y')
            return False
        except:
            return True
        
def generateDogInfoString(dog):
    dogInfoString = f"{dog.name}: "
    if dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK:
        dogInfoString += f"DHLPP #{dog.DHLPPComplete+1} on {stringifiedDate(dog.getNextDueDHLPPVaccine())}, "
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
            print(f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.")
        else:
            print(f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.")
        print("Thank you!\nThe LCDR Team\n\n")

    print("This completes the vaccines for the week, good job!")

def generateMessagesInShellAdopted(adoptableDogsNeedingVaccines):
    fostersToNotify = dict()

    for dog in adoptableDogsNeedingVaccines:
        print(f"\n\nYour Pup has the following vaccines due in the next week: \n ")
        print(generateDogInfoString(dog))
        if dog.vaccinePerson != "":
            print(f"\nYour vaccine volunteer is {dog.vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.")
        else:
            print(f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.")
        print("Thank you!\nThe LCDR Team\n\n")

    print("This completes the vaccines for the week, good job!")

def generateVaccinePersonReport(adoptableDogsNeedingVaccines):
    vaccinePeople = dict()
    print("VaxPerson | min # chats | DHLPP | Bord | chips")
    for dog in adoptableDogsNeedingVaccines:
        vaccinePerson = "Unknown"
        if dog.vaccinePerson and dog.vaccinePerson != '':
            vaccinePerson = dog.vaccinePerson
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
                neededDHLPP+=1
            if dogHasBordetellaDue:
               neededBoard +=1
            if not isValidChipCode(dog.chipCode):
                neededChips += 1
                
        print("%s | %s | %s | %s | %s" % (person.center(9,' '), str(len(fosters)).center(11, ' '), str(neededDHLPP).center(5, ' '), str(neededBoard).center(4, " "), str(neededChips).center(5, " ")))
        
def exportMessagesToCSV(adoptableDogsNeedingVaccines):
    fostersToNotify = dict()
    for dog in adoptableDogsNeedingVaccines:
        foster = dog.foster
        if fostersToNotify.get(foster):
            fostersToNotify[foster].append(dog)
        else:
            fostersToNotify[foster] = [dog]
    fosters = fostersToNotify.keys();
    with open("../Output/messages.txt", "w", newline='') as csvFile:
        messageWriter = csv.writer(csvFile, delimiter='\n', quotechar = "\t")
        for foster in fosters:
            messageString = "";
            messageString += (f"\n\nHi {foster},\nYour foster(s) have the following vaccines due in the next week: \n ")
            for dog in fostersToNotify[foster]:
                messageString += (generateDogInfoString(dog)) + "\n"
            if fostersToNotify[foster][0].vaccinePerson != "":
                messageString += (f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.")
            else:
                messageString += (f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.")
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
        f.write("Your vaccine volunteer is {vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n\n")
        f.write("We don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n\n")
        f.write("There is an event this week on {DATE} at {PLACE}, you can bring your dog there for vaccines\n\n")
        for foster in fosters:
            f.write(f"\n\nHi {foster},\nYour foster(s) have the following vaccines due in the next week: \n ")
            for dog in fostersToNotify[foster]:
                f.write(generateDogInfoString(dog))
                f.write("\n")
            if fostersToNotify[foster][0].vaccinePerson != "":
                f.write(f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n")
            else:
                f.write(f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n")
            f.write("Thank you!\nThe LCDR Team\n\n")

        f.write("This completes the vaccines for the week, good job!")

def exportAdoptedDogMessagesToFile(adoptableDogsNeedingVaccines):
    filename = f"Adopted_Dog_messages_{stringifiedDateForFileName(TODAY)}.txt"
    fostersToNotify = dict()

    with open(filename, "w") as f:
        f.write("Your vaccine volunteer is {vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n\n")
        f.write("We don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n\n")
        f.write("There is an event this week on {DATE} at {PLACE}, you can bring your dog there for vaccines\n\n")
        for dog in adoptableDogsNeedingVaccines:
            f.write(f"\n\nYour Pup has the following vaccines due in the next week: \n ")
            f.write(generateDogInfoString(dog))
            if dog.vaccinePerson != "":
                f.write(f"\n\nYour vaccine volunteer is {dog.vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n")
            else:
                f.write(f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n")
            f.write("Thank you!\nThe LCDR Team\n\n")

        f.write("This completes the vaccines for the week, good job!")

def writeEventListToFile(dogsToWrite):
    filename = f"EventFile_{stringifiedDateForFileName(TODAY)}.csv"
    with open(filename, "w") as eventFile:
        eventWriter = csv.writer(eventFile)
        eventWriter.writerow(["Dog Name", "Chip", "DHLPP", "Board"])
        for dog in dogsToWrite:
            eventWriter.writerow([dog.name, dog.chipCode, dog.getNextDueDHLPPVaccine(), dog.getNextDueBordetellaVaccine()])


pathToAdoptableFile = "C:/Users/markr/OneDrive/Documents/Personal/LCDR/Adoptable_06_20_2024.csv"#input("Please enter the path to the adoptable dogs csv")
adoptableDogsNeedingVaccines = []
with open(pathToAdoptableFile, newline = '') as adoptableFile:
    readInDogs = 0;
    rowNumber = 0;
    dogsEligible = 0;
    adoptableReader = csv.reader(adoptableFile, delimiter=',', quotechar = '|')

    for row in adoptableReader:
        if rowNumber == 0 or rowNumber == 1:
            rowNumber+=1
            continue
        if(row[AdoptableColums.NAME.value]):
            rowNumber+=1
            dog = AdoptableDogRecord(row)
            dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
            dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
            if dogHasDHLPPDue or dogHasBordetellaDue :
                adoptableDogsNeedingVaccines.append(dog)
print(f"Got {len(adoptableDogsNeedingVaccines)} adoptable dogs that need vaccines")

pathToAdoptedFile =  "C:/Users/markr/OneDrive/Documents/Personal/LCDR/Adopted_06_20_2024.csv"# input("Please enter the path to the adopted dogs csv")
adoptedDogsNeedingVaccines = []
with open(pathToAdoptedFile, newline = '') as adoptedFile:
    readInDogs = 0;
    rowNumber = 0;
    dogsEligible = 0;
    adoptedReader = csv.reader(adoptedFile, delimiter=',', quotechar = '|')
    for row in adoptedReader:
        if rowNumber == 0 or rowNumber == 1:
            rowNumber+=1
            continue
        if(row[AdoptedColums.LCDR_NAME.value]):
            rowNumber+=1
            dog = AdoptedDogRecord(row)
            dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
            dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
            if dogHasDHLPPDue or dogHasBordetellaDue :
                adoptedDogsNeedingVaccines.append(dog)
print(f"Got {len(adoptedDogsNeedingVaccines)} adopted dogs that need vaccines")

allDogsNeedingVaccines = adoptableDogsNeedingVaccines + adoptedDogsNeedingVaccines
print("Adoptable: ")
for dog in adoptableDogsNeedingVaccines:
    print(generateDogInfoString(dog))
print()
print("Adopted: ")
for dog in adoptedDogsNeedingVaccines:
    print(generateDogInfoString(dog))
print()
generateVaccinePersonReport(allDogsNeedingVaccines)
exportAdoptableDogMessagesToFile(adoptableDogsNeedingVaccines)
exportAdoptedDogMessagesToFile(adoptedDogsNeedingVaccines)
writeEventListToFile(allDogsNeedingVaccines)
