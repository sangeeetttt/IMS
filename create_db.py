import sqlite3

def create_db():
    con = sqlite3.connect(database= r'ims.db')
    cur= con.cursor()
    cur.ececute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text,gender, contact text, dob text,doj text,pass text, utype text, adress text, salary text)")
    con.commit()



create_db()
