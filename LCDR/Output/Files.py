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
            f.write("Please bring your records trifold to your appointment\n")
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
    worksheet.append(["Dog Name", "Vaccine Volunteer", "Chip", "DHLPP", "DHLPP #", "Bord", "Bord #"])
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

# Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                       showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style

    worksheet.add_table(tab)

    workbook.save(filename = filename)