__author__ = '610280'
from xlrd import open_workbook

FIRST_ROW = 0
SECOND_ROW = 1

book = open_workbook('examples.xlsx')
sheet = book.sheet_by_index(0)

#LABEL ROWS(1 and 2)
row_one = [sheet.cell(FIRST_ROW, col).value for col in range(sheet.ncols)]
row_two = [sheet.cell(SECOND_ROW, col).value for col in range(sheet.ncols)]

#FORMAT and MERGE into one to eliminate empty cells
columns = row_one[:5] + row_two[5:9] + row_one[10:]
print(columns)

dict_list = []
# for row_index in range(1, sheet.nrows):
#     sheet.cell(row_index, col_index).value

