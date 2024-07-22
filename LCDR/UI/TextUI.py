import openpyxl

from LCDR.Excel.ColumnNames import HEADER_ROW, INFO_ROW, AdoptableColums
from LCDR.Excel.DataParser.ColorInterpretor import getCellColor, CellColor
from LCDR.Excel.DataParser.DogModels import AdoptableDogRecord, AdoptedDogRecord
from LCDR.Excel.DataParser.TypeChecker import isValidChipCode
from LCDR.Output.Files import exportAdoptableDogMessagesToFile, exportAdoptedDogMessagesToFile, \
    writeEventListToExcelFile
from LCDR.Output.PNG import generateVaccinePersonReportPNG, generateVaccinePersonImage
from LCDR.Output.Shell import generateVaccinePersonReport
from LCDR.Utils import stringifiedDateForFileName, TODAY, NEXT_WEEK, getDogCountsByFoster


def textUI():
    PATH_TO_FILE = "../Data Files/LCDR_Dog_Sheet_07_22_2024.xlsx"
    if not os.path.exists(f"../Output/{stringifiedDateForFileName(TODAY)}"):
        os.makedirs(f"../Output/{stringifiedDateForFileName(TODAY)}")
    wb = openpyxl.load_workbook(PATH_TO_FILE, data_only=True)
    ws = wb.worksheets[0]
    rowNum = 0
    redCell = ws.cell(19, 2)
    print(getCellColor(redCell))
    adoptableDogsWithNeeds = []
    adoptedDogsWithNeeds = []
    for row in ws:
        rowNum += 1
        if rowNum == HEADER_ROW or rowNum == INFO_ROW:
            continue
        if getCellColor(row[AdoptableColums.NAME.value]) == CellColor.PALE_PINK.value:
            continue
        if not row[AdoptableColums.NAME.value].value == None:
            dog = AdoptableDogRecord(row)
        else:
            break
        if getCellColor(row[AdoptableColums.VACCINE_PERSON.value]) == CellColor.BRIGHT_GREEN.value:
            continue
        dogHasDHLPPDue = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
        dogHasBordetellaDue = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
        if dogHasDHLPPDue or dogHasBordetellaDue:
            adoptableDogsWithNeeds.append(dog)
        if (dog.name == None):
            break
    print(f"There are {len(adoptableDogsWithNeeds)} adoptable pups that need a vaccine")
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
    print(f"There are {len(adoptedDogsWithNeeds)} adopted pups that need a vaccine")
    allDogsWithNeeds = adoptableDogsWithNeeds + adoptedDogsWithNeeds
    generateVaccinePersonReport(allDogsWithNeeds)
    exportAdoptableDogMessagesToFile(adoptableDogsWithNeeds)
    exportAdoptedDogMessagesToFile(adoptedDogsWithNeeds)
    writeEventListToExcelFile(allDogsWithNeeds)
    generateVaccinePersonReportPNG(allDogsWithNeeds)
    generateVaccinePersonImage(allDogsWithNeeds)
    fostersToContact = getDogCountsByFoster(allDogsWithNeeds)
    neededDHLPP = 0;
    neededBord = 0;
    neededChips = 0;
    for dog in allDogsWithNeeds:
        dogNeedsDLHPP = dog.getNextDueDHLPPVaccine() and dog.getNextDueDHLPPVaccine() <= NEXT_WEEK
        dogNeedsMicroChip = not isValidChipCode(dog.chipCode)
        dogNeedsBordetella = dog.getNextDueBordetellaVaccine() and dog.getNextDueBordetellaVaccine() <= NEXT_WEEK
        if dogNeedsDLHPP:
            neededDHLPP += 1
        if dogNeedsBordetella:
            neededBord += 1
        if dogNeedsMicroChip:
            neededChips += 1


    print()
    print(f"There are {len(fostersToContact)} chats to interact with, "
          f"needing a total of {neededDHLPP} 5/1s, {neededBord} bordetella vaccines, and {neededChips} microchips")
