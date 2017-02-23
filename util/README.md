# DB Management Script
Utility that resets the database in short commands.

## Apartment & Landlord Models
__Load data__  
Creates objects in the database based on the entries from the excel spreadsheet. Spreadsheet path must be specified.

```
python script load <xlsx path>
python script load /home/jackson/Downloads/Project\ PLASE\ DB.xlsx
```

__Purge data__  
Removes all data in the Apartment and Landlord models. Unlike the `flush` via `manage.py`, this command does not affect other objects such as existing user.

```
python script purge
```
