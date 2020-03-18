import openpyxl as op


wb = op.load_workbook('madreseye taht app.xlsx')
sheet = wb['Classes']

name = sheet.cell(row=1, column=1).value
print(name)