import csv

import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

from LCDR.DataModels.Dog import generateDogInfoString
from LCDR.Utils import TODAY, NEXT_WEEK, stringifiedDateForFileName, stringifiedDate
from LCDR.Excel.DataParser.TypeChecker import isValidChipCode


def exportMessagesToCSV(adoptableDogsNeedingVaccines, outputPath):
    fostersToNotify = dict()
    for dog in adoptableDogsNeedingVaccines:
        foster = dog.foster
        if fostersToNotify.get(foster):
            fostersToNotify[foster].append(dog)
        else:
            fostersToNotify[foster] = [dog]
    fosters = fostersToNotify.keys();
    with open(f"{outputPath}/{stringifiedDateForFileName(TODAY)}/messages.txt", "w", newline='') as csvFile:
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


def exportAdoptableDogMessagesToFile(adoptableDogsNeedingVaccines, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/Adoptable_Dog_messages_{stringifiedDateForFileName(TODAY)}.txt"
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
            f.write(f"\n\nHi {foster},\nYour foster(s) have the following vaccines due in the next week: \n")
            for dog in fostersToNotify[foster]:
                f.write(f"\t{generateDogInfoString(dog)}\n")
            if fostersToNotify[foster][0].vaccinePerson and fostersToNotify[foster][0].vaccinePerson != "":
                f.write(
                    f"\nYour vaccine volunteer is {fostersToNotify[foster][0].vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n")
            else:
                f.write(
                    f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n")
            f.write("Vaccines can be given up to 3 days before or 3 days after the due date.\n")
            f.write("Thank you!\nThe LCDR Team\n\n")

        f.write("This completes the vaccines for the week, good job!")


def exportAdoptedDogMessagesToFile(adoptableDogsNeedingVaccines, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/Adopted_Dog_messages_{stringifiedDateForFileName(TODAY)}.txt"
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
            f.write(f"\n\nYour Pup has the following vaccines due in the next week: \n")
            f.write(f"\t{generateDogInfoString(dog)}\n")
            if dog.vaccinePerson and dog.vaccinePerson != "":
                f.write(
                    f"\nYour vaccine volunteer is {dog.vaccinePerson}, they will let you know their availability and you can coordinate from there on date/time/location.\n")
            else:
                f.write(
                    f"\nWe don't have a vaccine person on-file for you, please let us know who is closest to you from the list below, and we will get them added and tagged.\n")
            f.write("Vaccines can be given up to 3 days before or 3 days after the due date.\n")
            f.write("If you have picked up your records, please bring them with you to the appointment. \n")
            f.write("Thank you!\nThe LCDR Team\n\n")

        f.write("This completes the vaccines for the week, good job!")


def writeEventListToCSVFile(dogsToWrite, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/EventFile_{stringifiedDateForFileName(TODAY)}.csv"
    with open(filename, "w", newline='\n') as eventFile:
        eventWriter = csv.writer(eventFile)
        eventWriter.writerow(["Dog Name", "Vaccine Volunteer", "Chip", "DHLPP", "DHLPP #", "Bord", "Bord #"])
        for dog in dogsToWrite:
            nextDueDHLPP = dog.getNextDueDHLPPVaccine()
            dhlppDue = dog.DHLPPComplete + 1;
            if (nextDueDHLPP != None and nextDueDHLPP <= NEXT_WEEK):
                nextDueDHLPP = stringifiedDate(nextDueDHLPP);
            else:
                nextDueDHLPP = ""
                dhlppDue = ""
            nextDueBord = dog.getNextDueBordetellaVaccine()
            dueBordNumber = dog.BordetellaComplete + 1
            if nextDueBord != None and nextDueBord <= NEXT_WEEK:
                nextDueBord = stringifiedDate(nextDueBord)
            else:
                nextDueBord = ""
                dueBordNumber = ""
            chipCode = ""
            if not isValidChipCode(dog.chipCode):
                try:
                    chipCode = stringifiedDate(dog.chipCode)
                except:
                    chipCode = dog.chipCode
            eventWriter.writerow(
                [dog.name, dog.vaccinePerson, chipCode, nextDueDHLPP, dhlppDue, nextDueBord, dueBordNumber]
            )

def writeEventListToExcelFile(dogsToWrite, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/EventFile_{stringifiedDateForFileName(TODAY)}.xlsx"
    workbook = openpyxl.Workbook();
    worksheet = workbook.active
    worksheet.append(["Dog Name", "Vaccine Volunteer", "Chip", "DAPPv [5/1]", "DAPPv [5/1] #", "Bord", "Bord #"])
    for dog in dogsToWrite:
        nextDueDHLPP = dog.getNextDueDHLPPVaccine()
        dhlppDue = dog.DHLPPComplete + 1;
        if (nextDueDHLPP != None and nextDueDHLPP <= NEXT_WEEK):
            nextDueDHLPP = stringifiedDate(nextDueDHLPP);
        else:
            nextDueDHLPP = ""
            dhlppDue = ""
        nextDueBord = dog.getNextDueBordetellaVaccine()
        dueBordNumber = dog.BordetellaComplete + 1
        if nextDueBord != None and nextDueBord <= NEXT_WEEK:
            nextDueBord = stringifiedDate(nextDueBord)
        else:
            nextDueBord = ""
            dueBordNumber = ""
        chipCode = ""
        if not isValidChipCode(dog.chipCode):
            try:
                chipCode = stringifiedDate(dog.chipCode)
            except:
                chipCode = dog.chipCode
        worksheet.append(
            [dog.name, dog.vaccinePerson, chipCode, nextDueDHLPP, dhlppDue, nextDueBord, dueBordNumber]
        )
    tab = Table(displayName="DogEventTable", ref=f"A1:G{len(dogsToWrite) + 1}")

# Add a default style with striped rows and columns
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                       showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style

    worksheet.add_table(tab)

    workbook.save(filename = filename)
def writeRabiesNeedsToTXTFile(dogsToWrite, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/Rabies_Dogs_{stringifiedDateForFileName(TODAY)}.txt"
    with open(filename, "w") as f:
        for dog in dogsToWrite:
            f.write(f"{dog.name}: {dog.getNextRabiesDate()}\n")

def writeVaccineVolunteerReportToXLSX(dogsWithVaccinesDue, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/VolunteerReport_{stringifiedDateForFileName(TODAY)}.xlsx"
    workbook = openpyxl.Workbook();
    worksheet = workbook.active
    worksheet.append(["Vaccine Volunteer", "# of chats", "5/1", "Bord", "Chips"])
    vaccinePeople = dict()
    for dog in dogsWithVaccinesDue:
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
    personNumber = 0
    for person in sortedKeys:
        personNumber += 1
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
        worksheet.append(
            [person, len(fosters), neededDHLPP, neededBoard, neededChips]
        )
    tab = Table(displayName="DogEventTable", ref=f"A1:E{len(dogsWithVaccinesDue) + 1}")

    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style

    worksheet.add_table(tab)

    workbook.save(filename = filename)
