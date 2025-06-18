import os

import openpyxl

from LCDR.Excel.ColumnNames import HEADER_ROW, INFO_ROW, getAdoptableColumnIndexs, \
    getAdoptedColumnIndex
from LCDR.Excel.DataParser.ColorInterpretor import getCellColor, CellColor
from LCDR.Excel.DataParser.DogModels import AdoptableDogRecord, AdoptedDogRecord
from LCDR.Output.Files import exportAdoptableDogMessagesToFile, exportAdoptedDogMessagesToFile, \
    writeEventListToExcelFile, writeVaccineVolunteerReportToXLSX
from LCDR.Output.PNG import generateVaccinePersonImage, generateVaccinePersonReportPNG, generateSummaryTable
from LCDR.Utils import stringifiedDateForFileName, TODAY, dateBetween, NEXT_WEEK, LAST_45_DAYS, NEXT_45_DAYS, \
    sortListOfDogsInLocationOrder


def readInDogs(filepath):
    PATH_TO_FILE = filepath
    wb = openpyxl.load_workbook(PATH_TO_FILE, data_only=True)
    ws = wb.worksheets[0]
    rowNum = 0
    adoptableDogs = []
    adoptedDogs = []
    emptyRows = 0
    columnIndexDict = dict()
    for row in ws:
        rowNum += 1
        if rowNum == INFO_ROW:
            continue
        if rowNum == HEADER_ROW:
            columnIndexDict = getAdoptableColumnIndexs(row)
        if getCellColor(row[columnIndexDict["NAME"]]) == CellColor.PALE_PINK.value:
            continue
        if not row[columnIndexDict["NAME"]].value is None:
            dog = AdoptableDogRecord(row, columnIndexDict)
            adoptableDogs.append(dog)
            emptyRows = 0

        else:
            emptyRows += 1
            if(emptyRows >= 20):
                break

    ws = wb.worksheets[1]
    rowNum = 0
    for row in ws:
        rowNum += 1
        if rowNum == INFO_ROW:
            continue
        if rowNum == HEADER_ROW:
            columnIndexDict = getAdoptedColumnIndex(row)
        dog = AdoptedDogRecord(row, columnIndexDict)
        print(dog)
        if getCellColor(row[columnIndexDict["VACCINE_PERSON"]]) == CellColor.BRIGHT_GREEN.value or getCellColor(row[columnIndexDict["NAME"]]) == CellColor.PALE_PINK.value:
            continue
        adoptedDogs.append(dog)
    return [adoptableDogs, adoptedDogs]


def generateFiles(adoptableDogsWithNeeds, adoptedDogsWithNeeds, outputPath = "./Output"):
    if not os.path.exists(f"{outputPath}/{stringifiedDateForFileName(TODAY)}"):
        os.makedirs(f"{outputPath}/{stringifiedDateForFileName(TODAY)}", exist_ok=True)
    allDogsWithNeeds = adoptableDogsWithNeeds + adoptedDogsWithNeeds
    exportAdoptableDogMessagesToFile(adoptableDogsWithNeeds, outputPath)
    exportAdoptedDogMessagesToFile(adoptedDogsWithNeeds, outputPath)
    # sortedAllDogsWithNeeds = sortListOfDogsInLocationOrder(allDogsWithNeeds)
    writeEventListToExcelFile(allDogsWithNeeds, outputPath)
    writeVaccineVolunteerReportToXLSX(allDogsWithNeeds, outputPath)


def getDogsWithNeeds(candidateDogs):
    dogsWithNeeds = []
    for dog in candidateDogs:
        dhlpp = dog.getNextDueDHLPPVaccine()
        bord = dog.getNextDueBordetellaVaccine()
        if (dhlpp is not None and dateBetween(dhlpp, LAST_45_DAYS, NEXT_WEEK)) or (bord is not None and dateBetween(bord, LAST_45_DAYS, NEXT_WEEK)):
            dogsWithNeeds.append(dog)
    return dogsWithNeeds

def getOverdueDogs(canidateDogs):
    overdueDogs = []
    for dog in canidateDogs:
        dhlpp = dog.getNextDueDHLPPVaccine()
        bord = dog.getNextDueBordetellaVaccine()
        if (dhlpp is not None and dateBetween(dhlpp, LAST_45_DAYS, TODAY)) or (bord is not None and dateBetween(bord, LAST_45_DAYS, TODAY)):
            overdueDogs.append(dog)
    return overdueDogs

def getRabiesDogs(canidateDogs):
    rabiesDogs = []
    for dog in canidateDogs:
        if(dog.getNextRabiesDate() is not None and dog.getNextRabiesDate() <= NEXT_45_DAYS):
            rabiesDogs.append(dog)
    return rabiesDogs


