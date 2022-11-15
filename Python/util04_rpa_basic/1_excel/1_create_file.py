from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "OraenoSheet"
wb.save("sample.xlsx")
wb.close()