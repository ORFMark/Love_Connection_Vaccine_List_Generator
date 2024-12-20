from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from LCDR.DataModels.Dog import generateDogInfoString, dogNeeds
from LCDR.Excel.DataParser.TypeChecker import isValidChipCode
from LCDR.Utils import stringifiedDateForFileName, TODAY, NEXT_WEEK, stringifiedDate


def generateVaccinePersonReportPNG(listOfDogs, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/Vaccine_Volunteer_Report_{stringifiedDateForFileName(TODAY)}.png"
    img = Image.new(mode = "RGB", size = (500,250))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r"C:\Users\markr\OneDrive\Documents\Personal\LCDR\UbuntuMono-B.ttf", 16)
    vaccinePeople = dict()
    draw.text((0,0), "   VaxPerson    | min # chats |  5/1  | Bord | chips", (255,255,255), font)
    for dog in listOfDogs:
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

        draw.text((0, (16*personNumber)), "%s | %s | %s | %s | %s" % (
            person.center(15, ' '), str(len(fosters)).center(11, ' '), str(neededDHLPP).center(5, ' '),
            str(neededBoard).center(4, " "), str(neededChips).center(5, " ")), (255,255,255), font)
        img.save(filename)

def generateVaccinePersonImage(listOfDogs, outputPath):
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/Vaccine_Volunteer_Breakout_{stringifiedDateForFileName(TODAY)}.png"
    img = Image.new(mode = "RGB", size = (500,40*len(listOfDogs)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r"C:\Users\markr\OneDrive\Documents\Personal\LCDR\UbuntuMono-B.ttf", 20)
    vaccinePeople = dict()
    for dog in listOfDogs:
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
    lineNumber = 0;
    draw.text((0,lineNumber), f"Vaccine Volunteer Dog Breakout {stringifiedDate(TODAY)}", (255,255,255), font)
    lineNumber += 1
    for volunteer in sortedKeys:
        fosters = dict()
        for dog in vaccinePeople[volunteer]:
            if dog.foster is None:
                dog.foster = "Unknown"
            if fosters.get(dog.foster):
                fosters[dog.foster].append(dog)
            else:
                fosters[dog.foster] = [dog]
        volunDHLPP = 0
        volunBord = 0
        volunChips = 0
        listOfFosters = list(fosters.keys())
        listOfFosters.sort()
        for foster in listOfFosters:
            for dog in fosters[foster]:
                needs = dogNeeds(dog)
                if needs[0]:
                    volunDHLPP += 1
                if needs[1]:
                    volunBord += 1
                if needs[2]:
                    volunChips += 1
        draw.text((0, lineNumber*20), f"Volunteer: {volunteer}", (255,255,255), font)
        lineNumber += 1

        for foster in listOfFosters:
            for dog in fosters[foster]:
                dispText =  f"\t\t\t\t{dog.name}"
                needs = dogNeeds(dog)
                if needs[0]:
                    dispText += " 5/1 "
                if needs[1]:
                    dispText += " Bord "
                if needs[2]:
                    dispText += " Chip "
                draw.text((0, lineNumber*20), dispText, (255,255,255), font)
                lineNumber += 1
        lineNumber += 1
    img.save(filename)

def generateSummaryTable(dogsToVaccinate, outputPath = "."):
    DOG_COLUMN_NAME = "Dog"
    VAX_VOL_COLUMN_NAME = "Volunteer"
    FIVE_IN_1_DATE_COLUMN_NAME = "DAPPv [5/1]"
    FIVE_IN_1_COUNT_COLUMN_NAME = "DAPPv [5/1]#"
    BORD_DATE_COLUMN_NAME = "Bord"
    BORD_COUNT_COLUM_NAME = "Bord #"
    filename = f"{outputPath}/{stringifiedDateForFileName(TODAY)}/Summary_Table_{stringifiedDateForFileName(TODAY)}.png"
    img = Image.new(mode = "RGB", size = (750,(len(dogsToVaccinate) + 2)*32))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r"C:\Users\markr\OneDrive\Documents\Personal\LCDR\UbuntuMono-B.ttf", 16)

    dogNameList = []
    volNameList = []

    for dog in dogsToVaccinate:
        if dog.name is not None:
            dogNameList.append(dog.name)
        else:
            dogNameList.append("")
        if dog.vaccinePerson is not None:
            volNameList.append(dog.vaccinePerson)
        else:
            volNameList.append("")
    nameColSize = findMaxLength(dogNameList)
    volColSize = findMaxLength(volNameList)
    draw.text((0, 0), "%s|%s|%s|%s|%s|%s" % (DOG_COLUMN_NAME.center(nameColSize + 2, ' '), VAX_VOL_COLUMN_NAME.center(volColSize+2, ' '), FIVE_IN_1_DATE_COLUMN_NAME.center(len(FIVE_IN_1_DATE_COLUMN_NAME) + 2, ' '),FIVE_IN_1_COUNT_COLUMN_NAME.center(len(FIVE_IN_1_COUNT_COLUMN_NAME) + 2, ' '),BORD_DATE_COLUMN_NAME.center(len("MM/DD/YYYY") + 2, ' '),BORD_COUNT_COLUM_NAME.center(len(BORD_COUNT_COLUM_NAME) + 2, ' ')), (255,255,255), font)
    draw.text((0, 16), "-"*(5+(nameColSize+2)+(volColSize+2)+(len(FIVE_IN_1_DATE_COLUMN_NAME)+2)+(len(FIVE_IN_1_COUNT_COLUMN_NAME) +2 ) + (len("MM/DD/YYYY") +2) + (len(BORD_COUNT_COLUM_NAME) + 2)), (255,255,255), font)
    lineNumber = 2
    for i in range(0, len(dogsToVaccinate)):
        dog = dogsToVaccinate[i]
        draw.text((0, lineNumber*16), "%s|%s|%s|%s|%s|%s" % (dog.name.center(nameColSize + 2, ' '), vaxVolString(dog).center(volColSize+2, ' '), stringifiedDate(dog.getNextDueDHLPPVaccine()).center(len(FIVE_IN_1_DATE_COLUMN_NAME) + 2, ' '), DAPPCountString(dog).center(len(FIVE_IN_1_COUNT_COLUMN_NAME) + 2, ' '), stringifiedDate(dog.getNextDueBordetellaVaccine()).center(len("MM/DD/YYYY") + 2, ' '), bordCountString(dog).center(len(BORD_COUNT_COLUM_NAME) + 2, ' ')), (255,255,255), font)
        lineNumber += 1
        draw.text((0, lineNumber*16), "-"*(5+(nameColSize+2)+(volColSize+2)+(len(FIVE_IN_1_DATE_COLUMN_NAME)+2)+(len(FIVE_IN_1_COUNT_COLUMN_NAME) +2 ) + (len("MM/DD/YYYY") +2) + (len(BORD_COUNT_COLUM_NAME) + 2)), (255,255,255), font)
        lineNumber += 1
        img.save(filename)
def findMaxLength(stringList):
    maxLength = -1
    for str in stringList:
        canidateLen = len(str)
        if(canidateLen > maxLength):
            maxLength = canidateLen
    return maxLength

def DAPPCountString(dog):
    if(dog.getNextDueDHLPPVaccine()):
        return str(dog.DHLPPComplete + 1)
    else:
        return ""
def bordCountString(dog):
    if(dog.getNextDueBordetellaVaccine()):
        return str(dog.BordetellaComplete + 1)
    else:
        return ""
def vaxVolString(dog):
    if(dog.vaccinePerson is not None):
        return dog.vaccinePerson
    else:
        return ""



