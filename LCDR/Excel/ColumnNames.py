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
    VACCINE_PERSON = 17
    DHLPP_1 = 18
    DHLPP_2 = 19
    DHLPP_3 = 20
    DHLPP_4 = 21
    DHLPP_5 = 22
    Bordetella_1 = 23
    Bordetella_2 = 24
    VACCINES_DUE_LOOP = 25
    PICTURE_IN_BIO = 26
    ALTER_DONE = 27
    AQUISITION_METHOD = 28
    GOOD_WITH_DOGS = 29
    GOOD_WITH_CATS = 30
    GOOD_WITH_KIDS = 31
    BEHAVIOR_NOTES = 32


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
    VACCINE_PERSON = 17
    DHLPP_1 = 18
    DHLPP_2 = 19
    DHLPP_3 = 20
    DHLPP_4 = 21
    DHLPP_5 = 22
    Bordetella_1 = 23
    Bordetella_2 = 24
    ADOPTED_NAME = 25
    ADOPTED_FAMILY = 26
    ADOPTED_FAMILY_CONTACT = 27
    ADOPTED_DATE = 28
    PAYMENT_COLLECTED = 29
    CONTRACT_COMPLETE = 30
    FOLLOWUP = 31
    NOTES = 32
