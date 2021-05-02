from Sqlite3Helper import *

db = Sqlite3Helper('warma.db')

print(db.query('SELECT * FROM videos'))