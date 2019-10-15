

import openpyxl
from openpyxl import load_workbook

exfile=load_workbook(filename="Book1.xlsx")
def functiontoinsert(userparameters, excelfilename ):
    sheet=exfile.active
    for string in userparameters:
        sheet[A(string.index+1):]