import re
from datetime import datetime

from LCDR.DataModels.Dog import Dog
from LCDR.Excel.DataParser.ColorInterpretor import doesCellCount, CellColor, getCellColor
from LCDR.Utils import DATE_PATTERN_4_DIGIT_YEAR, DATE_PATTERN_2_DIGIT_YEAR


class AdoptableDogRecord(Dog):
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
        if self.DHLPPComplete > 0:
            lastCompleteDAPPColName = str.format("DHLPP_{}", self.DHLPPComplete)
            indexOfLastDAPP = columnIndexDict[lastCompleteDAPPColName]
            print(str.format("Name: {}, Complete: {}, LastColor: {}", self.name, self.DHLPPComplete, getCellColor(excelRow[indexOfLastDAPP])))
            if getCellColor(excelRow[indexOfLastDAPP]) == CellColor.THREE_YEAR_GREEN.value:
                self.lastDAPPVaccineWas3Year = True;





class AdoptedDogRecord(Dog):
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