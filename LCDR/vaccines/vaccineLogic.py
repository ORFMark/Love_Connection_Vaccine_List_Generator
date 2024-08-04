import os

import openpyxl

from LCDR.Excel.ColumnNames import HEADER_ROW, INFO_ROW, AdoptableColums
from LCDR.Excel.DataParser.ColorInterpretor import getCellColor, CellColor
from LCDR.Excel.DataParser.DogModels import AdoptableDogRecord, AdoptedDogRecord
from LCDR.Output.Files import exportAdoptableDogMessagesToFile, exportAdoptedDogMessagesToFile, \
    writeEventListToExcelFile
from LCDR.Output.PNG import generateVaccinePersonImage, generateVaccinePersonReportPNG
from LCDR.Utils import stringifiedDateForFileName, TODAY, dateBetween, NEXT_WEEK


def readInDogs(filepath):
    PATH_TO_FILE = filepath
    wb = openpyxl.load_workbook(PATH_TO_FILE, data_only=True)
    ws = wb.worksheets[0]
    rowNum = 0
    adoptableDogs = []
    adoptedDogs = []
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
        adoptableDogs.append(dog)
    ws = wb.worksheets[1]
    rowNum = 0
    for row in ws:
        rowNum += 1
        if rowNum == HEADER_ROW or rowNum == INFO_ROW:
            continue
        dog = AdoptedDogRecord(row)
        if getCellColor(row[AdoptableColums.VACCINE_PERSON.value]) == CellColor.BRIGHT_GREEN.value or getCellColor(row[AdoptableColums.NAME.value]) == CellColor.PALE_PINK.value:
            continue
        adoptedDogs.append(dog)
    return [adoptableDogs, adoptedDogs]


def generateFiles(adoptableDogsWithNeeds, adoptedDogsWithNeeds, outputPath = None):
    if outputPath is None:
        outputPath = "./Output"
    if not os.path.exists(f"{outputPath}/{stringifiedDateForFileName(TODAY)}"):
        os.makedirs(f"{outputPath}/{stringifiedDateForFileName(TODAY)}", exist_ok=True)
    allDogsWithNeeds = adoptableDogsWithNeeds + adoptedDogsWithNeeds
    exportAdoptableDogMessagesToFile(adoptableDogsWithNeeds)
    exportAdoptedDogMessagesToFile(adoptedDogsWithNeeds)
    writeEventListToExcelFile(allDogsWithNeeds)
    generateVaccinePersonReportPNG(allDogsWithNeeds)
    generateVaccinePersonImage(allDogsWithNeeds)


def getDogsWithNeeds(candidateDogs):
    dogsWithNeeds = []
    for dog in candidateDogs:
        dhlpp = dog.getNextDueDHLPPVaccine()
        bord = dog.getNextDueBordetellaVaccine()
        if (dhlpp is not None and dateBetween(dhlpp, TODAY, NEXT_WEEK)) or (bord is not None and dateBetween(bord, TODAY, NEXT_WEEK)):
            dogsWithNeeds.append(dog)
    return dogsWithNeeds


def execute(inputFilePath):
    dogs = readInDogs(inputFilePath)
    adoptableDogsWithNeeds=getDogsWithNeeds(dogs[0])
    adoptedDogsWithNeeds=getDogsWithNeeds(dogs[1])
    generateFiles(adoptableDogsWithNeeds, adoptedDogsWithNeeds)
    return [adoptableDogsWithNeeds, adoptedDogsWithNeeds]
