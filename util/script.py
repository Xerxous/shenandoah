import loader
from xlrd import open_workbook

#xlsx reading
xlsx_path = '/home/jackson/Downloads/Project PLASE DB.xlsx'
            #input('Specify excel DB path(String input): ')
book = open_workbook(xlsx_path)

for index in loader.SHEET_INDICIES:
    sheet = book.sheet_by_index(index)
    li = loader.create_list(sheet, loader.COLUMNS[index], loader.ENTRY_START_ROW)
    db = loader.create_db(loader.COLUMNS[index], li)
    loader.load_db(db, index)
