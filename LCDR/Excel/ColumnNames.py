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
