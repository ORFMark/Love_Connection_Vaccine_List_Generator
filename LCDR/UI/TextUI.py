from LCDR.Output.Shell import generateVaccinePersonReport, generateSummarySentence
from LCDR.vaccines.vaccineLogic import readInDogs, generateFiles


def textUI():
    OUTPUT_DIRECTORY = "../Output"
    PATH_TO_FILE = input("Please enter the vaccine file path: ")
    dogs = readInDogs(PATH_TO_FILE)
    generateFiles(dogs[0], dogs[1], OUTPUT_DIRECTORY)
    generateVaccinePersonReport(dogs[0] + dogs[1] )
    generateSummarySentence(dogs[0] + dogs[1])

