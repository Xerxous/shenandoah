from xlrd import open_workbook
import os, sys, django, validate

SHEET_INDEX = 0
FIRST_ROW = 0
SECOND_ROW = 1
ENTRY_START_ROW = 2
ADDRESS_START = 5
ADDRESS_END = 10
XLSX_PATH = input('Specify excel DB path(String input): ')
DJANGO_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

#Django setup to import models
sys.path.append(DJANGO_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'plase.settings'
django.setup()
from search.models import Apartment, Landlord

#xlsx reading
book = open_workbook(XLSX_PATH)
sheet = book.sheet_by_index(SHEET_INDEX)
columns = ['agency', 'number', 'email', 'building', 'st_one', 'st_two', 'area', 'state', 'zipcode', 'low', 'high','cost_notes', 'rooms', 'studio', 'one_br', 'two_br', 'three_br', 'notes']

#row entries
entries = []
for col_index in range(len(columns)):
    col_list = []
    for row_index in range(ENTRY_START_ROW, sheet.nrows):
        val = validate.val(sheet.cell(row_index, col_index).value)
        col_list.append(val)
    entries.append(col_list)

#dictionary - key value pair of each columns label and a list of their entries
db = dict()
for index in range(len(columns)):
    db[columns[index]] = entries[index]
print(db)

for i in range(ENTRY_START_ROW, sheet.nrows):
    Apartment.objects.create(agency=db['agency'][i], number=db['number'][i], email=db['email'][i], building=db['building'][i], st_one=db['st_one'][i], st_two=db['st_two'][i], area=db['area'][i], state=db['state'][i], zipcode=db['zipcode'][i], low=db['low'][i], high=db['high'][i], cost_notes=db['cost_notes'][i], rooms=db['rooms'][i], studio=db['studio'][i], one_br=db['one_br'][i], two_br=db['two_br'][i], three_br=db['three_br'][i], notes=db['notes'][i])
    print('added' + db['agency'][i])
