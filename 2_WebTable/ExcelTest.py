import openpyxl

# workbook = openpyxl.load_workbook("D:\\Other_Notes\\Python\\Workspace\\1stFebPythonSelenium_Framework\\TestData\Data.xlsx")
workbook = openpyxl.load_workbook("D:\\Python\\Workspace\\8th-Aug-Selenium-2026\\TestData\\Demo1.xlsx")

sheet=workbook['Sheet1']     #workbook.active


rowSize=sheet.max_row
print(rowSize)


colSize=sheet.max_column
print(colSize)
