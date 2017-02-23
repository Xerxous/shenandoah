import sys
from xlrd import open_workbook
from tools import loader
from tools.loader import create_list, create_db, load_db, purge

if len(sys.argv) > 1:
    if sys.argv[1] == 'purge':
        purge()
    elif len(sys.argv) == 3 and sys.argv[1] == 'load':
        xlsx_path = sys.argv[2]
        book = open_workbook(xlsx_path)

        for index in loader.SHEET_INDICIES:
            sheet = book.sheet_by_index(index)
            li = create_list(sheet, loader.COLUMNS[index], loader.ENTRY_START_ROW)
            db = create_db(loader.COLUMNS[index], li)
            load_db(db, index)
    else:
        print('Invalid arguments: "load <xlsx path>" or "purge"')
else:
    print('Missing arguments: "load <xlsx path>" or "purge"')
