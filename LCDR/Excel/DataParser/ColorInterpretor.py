from enum import Enum


class CellColor(Enum):
    YELLOW = "FFFFFF00";
    RED = "FFFF0000";
    BRIGHT_GREEN = "FF00FF00";


def getCellColor(cell):
    return cell.fill.fgColor.index


def countColoredCells(cellColorCode, listOfCells):
    numOfColoredCells = 0;
    for cell in listOfCells:
        if getCellColor(cell) == cellColorCode:
            numOfColoredCells += 1
    return numOfColoredCells


def doesCellCount(excelRow, index):
    cell = excelRow[index]
    if getCellColor(cell) == CellColor.YELLOW.value or getCellColor(cell) == CellColor.RED.value:
        return False
    elif cell.value != "N/A" and cell.value != None and cell.value != "n/A":
        return True
