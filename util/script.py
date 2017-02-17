from xlrd import open_workbook
import os, sys, django

SHEET_INDEX = 0
FIRST_ROW = 0
SECOND_ROW = 1
ENTRY_START_ROW = 2
ADDRESS_START = 5
ADDRESS_END = 10
XLSX_PATH = '/home/jackson/examples.xlsx'
DJANGO_PATH = '/home/jackson/Projects/shenandoah/'

#Django setup to import models
sys.path.append(DJANGO_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'plase.settings'
django.setup()
from search.models import Apartment, Landlord

#xlsx reading
book = open_workbook(PATH)
sheet = book.sheet_by_index(SHEET_INDEX)

#LABEL ROWS(1 and 2)
row_one = [sheet.cell(FIRST_ROW, col).value for col in range(sheet.ncols)]
row_two = [sheet.cell(SECOND_ROW, col).value for col in range(sheet.ncols)]

#FORMAT and MERGE into one to eliminate empty cells
columns = row_one[:ADDRESS_START] + row_two[ADDRESS_START:ADDRESS_END] + row_one[ADDRESS_END:]

#row entries
entries = []
for col_index in range(len(columns)):
    col_list = []
    for row_index in range(ENTRY_START_ROW, sheet.nrows):
        col_list.append(sheet.cell(row_index, col_index).value)
    entries.append(col_list)

#dictionary - key value pair of each columns label and a list of their entries
dict_list = dict()
for index in range(len(columns)):
    dict_list[columns[index]] = entries[index]

#load in db
