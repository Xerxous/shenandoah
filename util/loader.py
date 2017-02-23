import models

ENTRY_START_ROW = 2
SHEET_INDICIES = [0, 1]
MODELS = ['Apartment', 'Landlord']
COLUMNS = [
    [
        'agency', 'number', 'email',
        'building', 'st_one', 'st_two',
        'area', 'state', 'zipcode',
        'low', 'high','cost_notes',
        'rooms', 'studio', 'one_br',
        'two_br', 'three_br', 'notes'
    ],
    [
        'individual', 'number', 'email',
        'st_one', 'st_two', 'city',
        'state', 'zipcode', 'low',
        'high', 'rooms', 'studio',
        'one_br', 'two_br', 'three_br',
        'notes'
    ]
]

def val(variable):
    return to_boolean(strip(integer(variable)))

def integer(variable):
    if type(variable)==float:
        return int(variable)
    return variable

def strip(variable):
    if type(variable)==int or type(variable)==type(None):
        return variable
    return variable.strip()

def to_boolean(variable):
    if variable == 'Yes':
        return True
    elif variable == 'No':
        return False
    return variable

def create_list(sheet, col, start_row):
    entries = []
    for col_index in range(len(col)):
        col_list = []
        for row_index in range(start_row, sheet.nrows):
            value = val(sheet.cell(row_index, col_index).value)
            col_list.append(value)
        entries.append(col_list)
    return entries

def create_db(col, entries):
    db = dict()
    for index in range(len(col)):
        db[col[index]] = entries[index]
    return db

def load_db(db, index):
    if index == 0:
        load_apt(db)
    else:
        load_landlord(db)

def load_apt(db):
    for i in range(len(db['agency'])):
        models.Apartment.objects.create(
            agency=db['agency'][i],
            number=db['number'][i],
            email=db['email'][i],
            building=db['building'][i],
            st_one=db['st_one'][i],
            st_two=db['st_two'][i],
            area=db['area'][i],
            state=db['state'][i],
            zipcode=db['zipcode'][i],
            low=db['low'][i],
            high=db['high'][i],
            cost_notes=db['cost_notes'][i],
            rooms=db['rooms'][i],
            studio=db['studio'][i],
            one_br=db['one_br'][i],
            two_br=db['two_br'][i],
            three_br=db['three_br'][i],
            notes=db['notes'][i])
        print('Added Apartment: ' + db['agency'][i])

def load_landlord(db):
    for i in range(len(db['individual'])):
        models.Landlord.objects.create(
            individual=db['individual'][i],
            number=db['number'][i],
            email=db['email'][i],
            st_one=db['st_one'][i],
            st_two=db['st_two'][i],
            city=db['city'][i],
            state=db['state'][i],
            zipcode=db['zipcode'][i],
            low=db['low'][i],
            high=db['high'][i],
            rooms=db['rooms'][i],
            studio=db['studio'][i],
            one_br=db['one_br'][i],
            two_br=db['two_br'][i],
            three_br=db['three_br'][i],
            notes=db['notes'][i])
        print('Added Private Landlord: ' + db['individual'][i])
