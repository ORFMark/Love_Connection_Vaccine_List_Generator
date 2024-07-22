import re
from datetime import datetime

from LCDR.DataModels.Dog import Dog
from LCDR.Excel.ColumnNames import AdoptableColums, AdoptedColums
from LCDR.Excel.DataParser.ColorInterpretor import doesCellCount
from LCDR.Utils import DATE_PATTERN_4_DIGIT_YEAR, DATE_PATTERN_2_DIGIT_YEAR


class AdoptableDogRecord(Dog):
    def __init__(self, excelRow):
        super().__init__()
        self.name = excelRow[AdoptableColums.NAME.value].value
        self.name = self.name.replace("*", '')
        self.name = self.name.strip()
        nameEnd = self.name.find("(")
        if nameEnd != -1:
            self.name = self.name[:nameEnd]
        self.gender = excelRow[AdoptableColums.GENDER.value].value
        self.foster = excelRow[AdoptableColums.FOSTER.value].value
        self.chipCode = excelRow[AdoptableColums.CHIP_CODE.value].value
        self.ageInMonths = excelRow[AdoptableColums.AGE_IN_MONTHS.value].value
        self.vaccinePerson = excelRow[AdoptableColums.VACCINE_PERSON.value].value
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_1.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_1.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_2.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_2.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_3.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_3.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_4.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_4.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptableColums.DHLPP_5.value].value)
        if doesCellCount(excelRow, AdoptableColums.DHLPP_5.value):
            self.DHLPPComplete += 1
        self.BordetellaDates.append(excelRow[AdoptableColums.Bordetella_1.value].value)
        if doesCellCount(excelRow, AdoptableColums.Bordetella_1.value):
            self.BordetellaComplete += 1
        self.BordetellaDates.append(excelRow[AdoptableColums.Bordetella_2.value].value)
        if doesCellCount(excelRow, AdoptableColums.Bordetella_2.value):
            self.BordetellaComplete += 1
        while ("N/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while ("N/a" in self.BordetellaDates):
            self.BordetellaDates.remove("N/a")
        while ("" in self.BordetellaDates):
            self.BordetellaDates.remove("")
        while ("Missing" in self.BordetellaDates):
            self.BordetellaDates.remove("Missing")
        while ("N/A" in self.DHLPPDates):
            self.DHLPPDates.remove("N/A")
        while ("N/a" in self.DHLPPDates):
            self.DHLPPDates.remove("N/a")
        while ("Missing" in self.DHLPPDates):
            self.DHLPPDates.remove("Missing")
        while ("" in self.DHLPPDates):
            self.DHLPPDates.remove("")
        for i in range(0, len(self.DHLPPDates)):
            if isinstance(self.DHLPPDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.DHLPPDates[i])
                if (result):
                    self.DHLPPDates[i] = datetime.strptime(result[0], "%m/%d/%Y")
        for i in range(0, len(self.BordetellaDates)):
            if isinstance(self.BordetellaDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.BordetellaDates[i])
                if (result):
                    self.BordetellaDates[i] = datetime.strptime(result[0], "%m/%d/%Y")




class AdoptedDogRecord(Dog):
    def __init__(self, excelRow):
        super().__init__()
        self.name = excelRow[AdoptedColums.LCDR_NAME.value].value
        self.gender = excelRow[AdoptedColums.GENDER.value].value
        self.foster = excelRow[AdoptedColums.FOSTER.value].value
        self.chipCode = excelRow[AdoptedColums.MICROCHIP.value].value
        self.ageInMonths = excelRow[AdoptedColums.AGE_IN_MONTHS.value].value
        self.vaccinePerson = excelRow[AdoptedColums.VACCINE_PERSON.value].value
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_1.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_1.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_2.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_2.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_3.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_3.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_4.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_4.value):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[AdoptedColums.DHLPP_5.value].value)
        if doesCellCount(excelRow, AdoptedColums.DHLPP_5.value):
            self.DHLPPComplete += 1
        self.BordetellaDates.append(excelRow[AdoptedColums.Bordetella_1.value].value)
        if doesCellCount(excelRow, AdoptedColums.Bordetella_1.value):
            self.BordetellaComplete += 1
        self.BordetellaDates.append(excelRow[AdoptedColums.Bordetella_2.value].value)
        if doesCellCount(excelRow, AdoptedColums.Bordetella_2.value):
            self.BordetellaComplete += 1
        while ("N/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while ("n/A" in self.BordetellaDates):
            self.BordetellaDates.remove("N/A")
        while ("N/a" in self.BordetellaDates):
            self.BordetellaDates.remove("N/a")
        while ("" in self.BordetellaDates):
            self.BordetellaDates.remove("")
        while ("Missing" in self.BordetellaDates):
            self.BordetellaDates.remove("Missing")
        while ("N/A" in self.DHLPPDates):
            self.DHLPPDates.remove("N/A")
        while ("N/a" in self.DHLPPDates):
            self.DHLPPDates.remove("N/a")
        while ("n/A" in self.DHLPPDates):
            self.DHLPPDates.remove("n/A")
        while ("Missing" in self.DHLPPDates):
            self.DHLPPDates.remove("Missing")
        while ("" in self.DHLPPDates):
            self.DHLPPDates.remove("")
        for i in range(0, len(self.DHLPPDates)):
            if isinstance(self.DHLPPDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.DHLPPDates[i])
                if (result):
                    self.DHLPPDates[i] = datetime.strptime(result[0], "%m/%d/%Y")
                else:
                    result = re.search(DATE_PATTERN_2_DIGIT_YEAR, self.DHLPPDates[i])
                    if (result):
                        self.DHLPPDates[i] = datetime.strptime(result[0], "%m/%d/%y")
        for i in range(0, len(self.BordetellaDates)):
            if isinstance(self.BordetellaDates[i], str):
                result = re.search(DATE_PATTERN_4_DIGIT_YEAR, self.BordetellaDates[i])
                if (result):
                    self.BordetellaDates[i] = datetime.strptime(result[0], "%m/%d/%Y")
        self.name = self.name.replace("*", '')
        self.name = self.name.strip()
        nameEnd = self.name.find("(")
        if nameEnd != -1:
            self.name = self.name[:nameEnd]
