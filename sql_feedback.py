import sqlite3
from sqlite3 import Error


def createfb_db(db):
    # Get a cursor object
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY, name TEXT , comment TEXT, cdate DATE)
        ''')
    db.commit()
    cursor = db.cursor()
    return cursor

def updatefb_db(db, name, comment, cdate):
    # Get a cursor object
    cursor = db.cursor()
    cursor.execute('''INSERT or REPLACE INTO feedback(name, comment, cdate)
                    VALUES(?,?,?)''', (name, comment, cdate))
    db.commit()   
    return cursor

def getallfb_db(cursor):
    cursor.execute('''SELECT name, comment, cdate FROM feedback''')
    all_rows = cursor.fetchall()
    return all_rows

def getrecentfb_db(cursor, limit):
    cursor.execute('''SELECT * FROM feedback ORDER by cdate DESC LIMIT (?)''', (limit,))
    all_rows = cursor.fetchall()
    return all_rows
