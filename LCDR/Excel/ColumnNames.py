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
    RECORDS = 0
    AdoptedPhoto = 1
    LCDR_NAME = 2
    GENDER = 3
    DOB = 4
    AGE_IN_MONTHS = 5
    INTAKE = 6
    MICROCHIP = 7
    COLOR = 8
    SIZE = 9
    BREED = 10
    LITTER = 11
    FOSTER = 12
    ALTER_DATE = 13
    RABIES_DATE = 14
    FECAL = 15
    SNAP = 16
    MED_NOTES = 17
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
