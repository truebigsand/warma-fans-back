import sqlite3

class Sqlite3Helper:
    def __init__(self,dbname):
        self.db = sqlite3.connect(dbname,check_same_thread=False)
    def query(self,sql):
        cur = self.db.cursor()
        cur.execute(sql)
        return cur.fetchall()
    def execute(self,sql):
        self.db.execute(sql)
    def __del__(self):
        self.db.commit()