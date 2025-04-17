import re
from datetime import datetime

from LCDR.DataModels.Dog import Dog
from LCDR.Excel.ColumnNames import AdoptableColums, AdoptedColums
from LCDR.Excel.DataParser.ColorInterpretor import doesCellCount, CellColor, getCellColor
from LCDR.Utils import DATE_PATTERN_4_DIGIT_YEAR, DATE_PATTERN_2_DIGIT_YEAR


class AdoptableDogRecord(Dog):
    def __init__(self, excelRow):
        super().__init__()
        self.name = str(excelRow[AdoptableColums.NAME.value].value)
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
        self.rabiesAdminDate = excelRow[AdoptableColums.RABIES_DATE.value].value
        if getCellColor(excelRow[AdoptableColums.RABIES_DATE.value]) == CellColor.YUCKY_GREEN.value:
            self.rabiesVaccineDuration = 3
        elif self.rabiesAdminDate is not None and self.rabiesAdminDate != "":
            self.rabiesVaccineDuration = 1
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

    def __init__(self, excelRow, columnIndexDict):
        super().__init__()
        self.name = str(excelRow[columnIndexDict["NAME"]].value)
        self.name = self.name.replace("*", '')
        self.name = self.name.strip()
        nameEnd = self.name.find("(")
        if nameEnd != -1:
            self.name = self.name[:nameEnd]
        self.gender = excelRow[columnIndexDict["GENDER"]].value
        self.foster = excelRow[columnIndexDict["FOSTER"]].value
        self.chipCode = excelRow[columnIndexDict["CHIP_CODE"]].value
        self.ageInMonths = excelRow[columnIndexDict["AGE_IN_MONTHS"]].value
        self.vaccinePerson = excelRow[columnIndexDict["VACCINE_PERSON"]].value
        self.rabiesAdminDate = excelRow[columnIndexDict["RABIES_DATE"]].value
        if getCellColor(excelRow[columnIndexDict["RABIES_DATE"]]) == CellColor.YUCKY_GREEN.value:
            self.rabiesVaccineDuration = 3
        elif self.rabiesAdminDate is not None and self.rabiesAdminDate != "":
            self.rabiesVaccineDuration = 1
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_1"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_1"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_2"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_2"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_3"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_3"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_4"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_4"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_5"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_5"]):
            self.DHLPPComplete += 1
        self.BordetellaDates.append(excelRow[columnIndexDict["Bordetella_1"]].value)
        if doesCellCount(excelRow, columnIndexDict["Bordetella_1"]):
            self.BordetellaComplete += 1
        self.BordetellaDates.append(excelRow[columnIndexDict["Bordetella_2"]].value)
        if doesCellCount(excelRow, columnIndexDict["Bordetella_2"]):
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
        self.name = str(excelRow[AdoptedColums.LCDR_NAME.value].value)
        self.gender = excelRow[AdoptedColums.GENDER.value].value
        self.foster = excelRow[AdoptedColums.FOSTER.value].value
        self.chipCode = excelRow[AdoptedColums.MICROCHIP.value].value
        self.ageInMonths = excelRow[AdoptedColums.AGE_IN_MONTHS.value].value
        self.vaccinePerson = excelRow[AdoptedColums.VACCINE_PERSON.value].value
        self.rabiesAdminDate = excelRow[AdoptedColums.RABIES_DATE.value].value
        if getCellColor(excelRow[AdoptableColums.RABIES_DATE.value]) == CellColor.YUCKY_GREEN.value:
            self.rabiesVaccineDuration = 3
        elif self.rabiesAdminDate is not None and self.rabiesAdminDate != "":
            self.rabiesVaccineDuration = 1
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
            self.BordetellaDates.remove("n/A")
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
        if self.name is not None:
            self.name = self.name.replace("*", '')
            self.name = self.name.strip()
            nameEnd = self.name.find("(")
            if nameEnd != -1:
                self.name = self.name[:nameEnd]

    def __init__(self, excelRow, columnIndexDict):
        super().__init__()
        self.name = str(excelRow[columnIndexDict["NAME"]].value)
        self.name = self.name.replace("*", '')
        self.name = self.name.strip()
        nameEnd = self.name.find("(")
        if nameEnd != -1:
            self.name = self.name[:nameEnd]
        self.gender = excelRow[columnIndexDict["GENDER"]].value
        self.foster = excelRow[columnIndexDict["FOSTER"]].value
        self.chipCode = excelRow[columnIndexDict["CHIP_CODE"]].value
        self.ageInMonths = excelRow[columnIndexDict["AGE_IN_MONTHS"]].value
        self.vaccinePerson = excelRow[columnIndexDict["VACCINE_PERSON"]].value
        self.rabiesAdminDate = excelRow[columnIndexDict["RABIES_DATE"]].value
        if getCellColor(excelRow[columnIndexDict["RABIES_DATE"]]) == CellColor.YUCKY_GREEN.value:
            self.rabiesVaccineDuration = 3
        elif self.rabiesAdminDate is not None and self.rabiesAdminDate != "":
            self.rabiesVaccineDuration = 1
        self.DHLPPDates = []
        self.DHLPPComplete = 0
        self.BordetellaDates = []
        self.BordetellaComplete = 0
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_1"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_1"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_2"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_2"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_3"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_3"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_4"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_4"]):
            self.DHLPPComplete += 1
        self.DHLPPDates.append(excelRow[columnIndexDict["DHLPP_5"]].value)
        if doesCellCount(excelRow, columnIndexDict["DHLPP_5"]):
            self.DHLPPComplete += 1
        self.BordetellaDates.append(excelRow[columnIndexDict["Bordetella_1"]].value)
        if doesCellCount(excelRow, columnIndexDict["Bordetella_1"]):
            self.BordetellaComplete += 1
        self.BordetellaDates.append(excelRow[columnIndexDict["Bordetella_2"]].value)
        if doesCellCount(excelRow, columnIndexDict["Bordetella_2"]):
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