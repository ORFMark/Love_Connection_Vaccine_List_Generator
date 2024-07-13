import openpyxl
wb = openpyxl.load_workbook('/path/file.xlsx', data_only=True)

# get first worksheet
ws = wb.worksheets[0]

# check first column in first 10 rows for fill color
for row in range(1, 10):
    cell = ws.cell(column=1, row=row)
    bgColor = cell.fill.bgColor.index
    fgColor = cell.fill.fgColor.index
    if bgColor != '00000000' or fgColor != '00000000':
        print(f"row {row}")
        print(f"  fgColor={fgColor}")
        print(f"  bgColor={bgColor}")
        print(f"  fillType={cell.fill.fill_type}")
        print(f"  value: {cell.value}")
