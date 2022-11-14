from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

ws.delete_rows(8,2)
wb.save("sample_delete_rows.xlsx")

ws.delete_cols(2)
wb.save("sample_delete_cols.xlsx")

