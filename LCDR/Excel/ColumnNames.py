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
    ALTER_DATE = 12
    RABIES_DATE = 13
    FECAL = 14
    SNAP = 15
    MED_NOTES = 16
    VACCINE_PERSON = 18
    DHLPP_1 = 19
    DHLPP_2 = 20
    DHLPP_3 = 21
    DHLPP_4 = 22
    DHLPP_5 = 23
    Bordetella_1 = 24
    Bordetella_2 = 25
    VACCINES_DUE_LOOP = 26
    PICTURE_IN_BIO = 27
    ALTER_DONE = 28
    AQUISITION_METHOD = 29
    GOOD_WITH_DOGS = 30
    GOOD_WITH_CATS = 31
    GOOD_WITH_KIDS = 32
    BEHAVIOR_NOTES = 33


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
    ALTER_DATE = 12
    RABIES_DATE = 13
    FECAL = 14
    SNAP = 15
    MED_NOTES = 16
    VACCINE_PERSON = 18
    DHLPP_1 = 19
    DHLPP_2 = 20
    DHLPP_3 = 21
    DHLPP_4 = 22
    DHLPP_5 = 23
    Bordetella_1 = 24
    Bordetella_2 = 25
    ADOPTED_NAME = 26
    ADOPTED_FAMILY = 27
    ADOPTED_FAMILY_CONTACT = 28
    ADOPTED_DATE = 29
    PAYMENT_COLLECTED = 30
    CONTRACT_COMPLETE = 31
    FOLLOWUP = 32
    NOTES = 33
