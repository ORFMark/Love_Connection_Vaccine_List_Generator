import csv

from LCDR.DataModels.Dog import generateDogInfoString
from LCDR.Utils import TODAY, NEXT_WEEK, stringifiedDateForFileName
from LCDR.Excel.DataParser.TypeChecker import isValidChipCode


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
