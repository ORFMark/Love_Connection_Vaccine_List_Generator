import math
import os

import openpyxl
import pygame

from LCDR.Excel.ColumnNames import AdoptableColums, HEADER_ROW, INFO_ROW
from LCDR.Excel.DataParser.ColorInterpretor import getCellColor, CellColor
from LCDR.Excel.DataParser.DogModels import AdoptableDogRecord, AdoptedDogRecord
from LCDR.Output.Files import writeEventListToExcelFile, exportAdoptedDogMessagesToFile, \
    exportAdoptableDogMessagesToFile
from LCDR.Output.PNG import generateVaccinePersonImage, generateVaccinePersonReportPNG
from LCDR.UI.Colors import RGBColors
from LCDR.UI.Graphical.ScreenObjects.InputBox import InputBox
from LCDR.UI.Graphical.ScreenObjects.TextDisplay import TextDisplay
from LCDR.Utils import NEXT_WEEK, getDogCountsByFoster, stringifiedDateForFileName, TODAY

PI = math.pi

SCREEN_SIZE = [600,400]
COLOR_ACTIVE = RGBColors.BLUE.value
COLOR_INACTIVE = RGBColors.GRAY.value

def generateFiles(filepath):
    PATH_TO_FILE = filepath
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
def GUI():
    pygame.init()
    FONT = pygame.font.Font (None, 50)
    screen=pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(RGBColors.WHITE.value)
    clock = pygame.time.Clock();
    pygame.display.set_caption("LCDR Vaccine List Generator")
    done = False
    buttonColor = COLOR_INACTIVE
    filePathInputBox = InputBox(pygame, 100, 100, 140, 32)
    filePathTextDescriptor = TextDisplay(pygame, 0, 100, "File Path")
    screenObjects = [filePathInputBox, filePathTextDescriptor]
    while not done:
        input_box = pygame.Rect(100, 100, 140, 32)

        clock.tick(30)
        screen.fill(RGBColors.WHITE.value)
        for object in screenObjects:
            object.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get(): ##checks the giant list of events
            if event.type==pygame.QUIT: ##handles quit event
                done = True
            for object in screenObjects:
                object.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    generateFiles(filePathInputBox.lastConfirmedValue)

    pygame.quit() ##ends pygame to make it idlefriendly
