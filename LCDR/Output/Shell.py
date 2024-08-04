from LCDR.Utils import NEXT_WEEK
from LCDR.Excel.DataParser.TypeChecker import isValidChipCode
from LCDR.DataModels.Dog import generateDogInfoString


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

def generateSummarySentence(adoptableDogs, adoptedDogs):
    allDogs = adoptableDogs + adoptedDogs
    needs = computeNeeds(allDogs)
    print(f"There are {len(adoptableDogs)} adoptable dogs and {len(adoptedDogs)} adopted dogs, who need a total of {needs[0]}  5/1, {needs[1]} Bord, and {needs[2]} chips")


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
