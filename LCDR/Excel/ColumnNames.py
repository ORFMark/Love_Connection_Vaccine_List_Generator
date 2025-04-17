import datetime
from enum import Enum


class DogSpreadsheetSheet(Enum):
    ADOPTABLE = 0
    ADOPTED = 1


INFO_ROW = 1
HEADER_ROW = 2


class AdoptableColums(Enum):
    FOLDER = 0
    NAME = 1
    GENDER = 2
    BIRTHDAY = 3
    AGE_IN_MONTHS = 4
    INTAKE_DATE = 5
    CHIP_CODE = 6
    COLOR = 7
    SIZE = 8
    BREED = 9
    LITTER = 10
    FOSTER = 11
    IS_FTA = 12
    ALTER_DATE = 13
    RABIES_DATE = 14
    FECAL = 15
    SNAP = 16
    MED_NOTES = 17
    JOT_FORM = 18
    VACCINE_PERSON = 19
    DHLPP_1 = 20
    DHLPP_2 = 21
    DHLPP_3 = 22
    DHLPP_4 = 23
    DHLPP_5 = 24
    Bordetella_1 = 25
    Bordetella_2 = 26
    VACCINES_DUE_LOOP = 27
    PICTURE_IN_BIO = 28
    ALTER_DONE = 29
    AQUISITION_METHOD = 30
    GOOD_WITH_DOGS = 31
    GOOD_WITH_CATS = 32
    GOOD_WITH_KIDS = 33
    BEHAVIOR_NOTES = 34


class AdoptedColums(Enum):
    RECORDS = 0;
    LCDR_NAME = 1
    GENDER = 2;
    DOB = 3
    AGE_IN_MONTHS = 4
    INTAKE = 5
    MICROCHIP = 6
    COLOR = 7
    SIZE = 8
    BREED = 9
    LITTER = 10
    FOSTER = 11
    IS_FTA = 12
    ALTER_DATE = 13
    RABIES_DATE = 14
    FECAL = 15
    SNAP = 16
    MED_NOTES = 17
    Jot_Form = 18
    VACCINE_PERSON = 19
    DHLPP_1 = 20
    DHLPP_2 = 21
    DHLPP_3 = 22
    DHLPP_4 = 23
    DHLPP_5 = 24
    Bordetella_1 = 25
    Bordetella_2 = 26
    ADOPTED_NAME = 27
    ADOPTED_FAMILY = 28
    ADOPTED_FAMILY_CONTACT = 29
    ADOPTED_DATE = 30
    PAYMENT_COLLECTED = 31
    CONTRACT_COMPLETE = 32
    FOLLOWUP = 33
    NOTES = 34

def getAdoptableColumnIndexs(rawHeaderRow):
    adoptableColumnDict = dict()
    headerRow = list()
    for cell in rawHeaderRow:
        headerRow.insert(len(headerRow), cell.value)
    print(headerRow)
    adoptableColumnDict["FOLDER"] = headerRow.index("Folder")
    adoptableColumnDict["NAME"] = headerRow.index("Name")
    adoptableColumnDict["GENDER"] = headerRow.index("Gender")
    adoptableColumnDict["BIRTHDAY"] = headerRow.index("DOB")
    adoptableColumnDict["AGE_IN_MONTHS"] = headerRow.index("Est Age In Months")
    adoptableColumnDict["INTAKE_DATE"] = headerRow.index("Intake Date")
    adoptableColumnDict["CHIP_CODE"] = headerRow.index("Microchip #")
    adoptableColumnDict["COLOR"] = headerRow.index("Color")
    adoptableColumnDict["SIZE"] = headerRow.index("EST. Size")
    adoptableColumnDict["BREED"] = headerRow.index("Breed")
    adoptableColumnDict["LITTER"] = headerRow.index("Litter Name")
    adoptableColumnDict["FOSTER"] = headerRow.index("Foster")
    adoptableColumnDict["IS_FTA"] = headerRow.index("FTA")
    adoptableColumnDict["ALTER_DATE"] = headerRow.index("Alter Date")
    adoptableColumnDict["RABIES_DATE"] = headerRow.index("Rabies Date")
    adoptableColumnDict["FECAL"] = headerRow.index("Fecal")
    adoptableColumnDict["SNAP"] = headerRow.index("Snap")
    adoptableColumnDict["MED_NOTES"] = 17
    adoptableColumnDict["JOT_FORM"] = 18
    adoptableColumnDict["VACCINE_PERSON"] = headerRow.index("Vax person")
    adoptableColumnDict["DHLPP_1"] = headerRow.index(datetime.datetime(2001, 5, 1, 0, 0))
    adoptableColumnDict["DHLPP_2"] = headerRow.index(datetime.datetime(2002, 5, 1, 0, 0))
    adoptableColumnDict["DHLPP_3"] = headerRow.index(datetime.datetime(2003, 5, 1, 0, 0))
    adoptableColumnDict["DHLPP_4"] = headerRow.index(datetime.datetime(2004, 5, 1, 0, 0))
    adoptableColumnDict["DHLPP_5"] = headerRow.index(datetime.datetime(2005, 5, 1, 0, 0))
    adoptableColumnDict["Bordetella_1"] = headerRow.index("Bordatella-1")
    adoptableColumnDict["Bordetella_2"] = headerRow.index("Bordatella-2")
    adoptableColumnDict["VACCINES_DUE_LOOP"] = headerRow.index("Vaccines Due")
    adoptableColumnDict["PICTURE_IN_BIO"] = headerRow.index("Picture in album")
    adoptableColumnDict["ALTER_DONE"] = headerRow.index("Alter Completed")
    adoptableColumnDict["AQUISITION_METHOD"] = headerRow.index("How did we acquire")
    adoptableColumnDict["GOOD_WITH_DOGS"] = headerRow.index("Dogs- Size?")
    adoptableColumnDict["GOOD_WITH_CATS"] = headerRow.index("Cats Y/N")
    adoptableColumnDict["GOOD_WITH_KIDS"] = headerRow.index("Kids?")
    adoptableColumnDict["BEHAVIOR_NOTES"] = headerRow.index("Behavior Notes")
    return adoptableColumnDict

def getAdoptedColumnIndex(rawHeaderRow):
    adoptedColumnIndexDict = dict()
    headerRow = list()
    for cell in rawHeaderRow:
        headerRow.insert(len(headerRow), cell.value)
    print(headerRow)
    adoptedColumnIndexDict["Folder"] = headerRow.index("Records Comp. X")
    adoptedColumnIndexDict["NAME"] = headerRow.index("LCDR Name")
    adoptedColumnIndexDict["GENDER"] = headerRow.index("Gender")
    adoptedColumnIndexDict["BIRTHDAY"] = headerRow.index("DOB")
    adoptedColumnIndexDict["AGE_IN_MONTHS"] = headerRow.index("Est Age In Months")
    adoptedColumnIndexDict["INTAKE_DATE"] = headerRow.index("Intake Date")
    adoptedColumnIndexDict["CHIP_CODE"] = headerRow.index("Microchip #")
    adoptedColumnIndexDict["COLOR"] = headerRow.index("Color")
    adoptedColumnIndexDict["SIZE"] = headerRow.index("Est. Size")
    adoptedColumnIndexDict["BREED"] = headerRow.index("Breed")
    adoptedColumnIndexDict["LITTER"] = headerRow.index("Litter Name")
    adoptedColumnIndexDict["FOSTER"] = headerRow.index("Foster")
    adoptedColumnIndexDict["IS_FTA"] = 12
    adoptedColumnIndexDict["ALTER_DATE"] = headerRow.index("Alter Date")
    adoptedColumnIndexDict["RABIES_DATE"] = headerRow.index("Rabies Date")
    adoptedColumnIndexDict["FECAL"] = headerRow.index("Fecal")
    adoptedColumnIndexDict["SNAP"] = headerRow.index("Snap")
    adoptedColumnIndexDict["MED_NOTES"] = 17
    adoptedColumnIndexDict["JOT_FORM"] = 18
    adoptedColumnIndexDict["VACCINE_PERSON"] = headerRow.index("Vax person")
    adoptedColumnIndexDict["DHLPP_1"] = headerRow.index(datetime.datetime(2001, 5, 1, 0, 0))
    adoptedColumnIndexDict["DHLPP_2"] = headerRow.index(datetime.datetime(2002, 5, 1, 0, 0))
    adoptedColumnIndexDict["DHLPP_3"] = headerRow.index(datetime.datetime(2003, 5, 1, 0, 0))
    adoptedColumnIndexDict["DHLPP_4"] = headerRow.index(datetime.datetime(2004, 5, 1, 0, 0))
    adoptedColumnIndexDict["DHLPP_5"] = headerRow.index(datetime.datetime(2005, 5, 1, 0, 0))
    adoptedColumnIndexDict["Bordetella_1"] = headerRow.index("Bordatella-1")
    adoptedColumnIndexDict["Bordetella_2"] = headerRow.index("Bordatella-2")
    return adoptedColumnIndexDict
