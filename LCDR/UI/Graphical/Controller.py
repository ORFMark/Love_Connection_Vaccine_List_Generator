import math

import pygame

from LCDR.UI.Colors import RGBColors
from LCDR.UI.Graphical.ScreenObjects.InputBox import InputBox
from LCDR.UI.Graphical.ScreenObjects.TextDisplay import TextDisplay
from LCDR.Utils import computeNeeds
from LCDR.vaccines.vaccineLogic import readInDogs, getDogsWithNeeds, generateFiles, getOverdueDogs

PI = math.pi

SCREEN_SIZE = [600,400]
COLOR_ACTIVE = RGBColors.BLUE.value
COLOR_INACTIVE = RGBColors.GRAY.value


def GUI():
    pygame.init()
    FONT = pygame.font.Font (None, 50)
    screen=pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(RGBColors.WHITE.value)
    clock = pygame.time.Clock();
    pygame.display.set_caption("LCDR Vaccine List Generator")
    done = False
    buttonColor = COLOR_INACTIVE
    filePathInputBox = InputBox(pygame, 100, 50, 250, 32)
    filePathTextDescriptor = TextDisplay(pygame, 0, 50, "File Path")
    adoptableDogs = TextDisplay(pygame, 0, 100, "Adoptable Dogs: ?")
    adoptedDogs = TextDisplay(pygame, 0, 150, "Adopted Dogs: ?")
    neededDLHPP = TextDisplay(pygame, 300, 200, "5/1: ?")
    neededBord = TextDisplay(pygame, 300, 100, "Bord: ?")
    neededChips = TextDisplay(pygame, 300, 150, "Chips: ?")
    overdueDogs = TextDisplay(pygame, 0, 200, "Overdue Dogs: ?")
    screenObjects = [filePathInputBox, filePathTextDescriptor, adoptableDogs, adoptedDogs, neededDLHPP, neededBord, neededChips, overdueDogs]
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
                    try:
                        pupLists = execute(filePathInputBox.lastConfirmedValue)
                        overdueDogs = getOverdueDogs(pupLists[0] + pupLists[1])
                        resorces = computeNeeds(pupLists[0] + pupLists[1])
                        screenObjects[2].text = f"Adoptable Dogs: {len(pupLists[0])}"
                        screenObjects[3].text = f"Adopted Dogs: {len(pupLists[1])}"
                        screenObjects[4].text = f"5/1: {resorces[0]}"
                        screenObjects[5].text = f"Bord: {resorces[1]}"
                        screenObjects[6].text = f"Chips: {resorces[2]}"
                        screenObjects[7].text = f"Overdue Dogs: {len(overdueDogs)}"
                    except Exception as e:
                        screenObjects[2].text = f"{e}"
                        screenObjects[3].text = ""
                        screenObjects[4].text = ""
                        screenObjects[5].text = ""
                        screenObjects[6].text = ""
                        screenObjects[7].text = ""


    pygame.quit() ##ends pygame to make it idlefriendly


def execute(inputFilePath):
    dogs = readInDogs(inputFilePath)
    adoptableDogsWithNeeds=getDogsWithNeeds(dogs[0])
    adoptedDogsWithNeeds=getDogsWithNeeds(dogs[1])
    generateFiles(adoptableDogsWithNeeds, adoptedDogsWithNeeds, "./Output")
    return [adoptableDogsWithNeeds, adoptedDogsWithNeeds]
