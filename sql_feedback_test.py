import sqlite3
from sqlite3 import Error

import datetime
from datetime import datetime, date, timedelta


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


def main():
    #database = r"C:\Users\bhpudipe\Documents\BackupSep2019\Documents\mosaic\tickerfb.db"
    database = ':memory:' # in-memory

    # CREATE a database in RAM or file
    db = sqlite3.connect(database)

    cursor = createfb_db(db)

    # INITIALLIZE DB (called users) with some entries
    name1 = 'John'
    comment1 = 'how are you?'
    udate1 = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
    updatefb_db(db, name1, comment1, udate1)

    name2 = 'Mary'
    comment2 = 'Today is a great day!'
    udate2 = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    updatefb_db(db, name2, comment2, udate2)

    name3 = 'Mike'
    comment3 = "Let us go home now, I'm tired"
    udate3 = date.today().strftime('%Y-%m-%d')
    updatefb_db(db, name3, comment3, udate3)

    print("GETTING All rows from db: ")
    all_rows = getallfb_db(cursor)
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns 2nd column (score)
        print('\t{0} : {1}: {2}'.format(row[2], row[0], row[1]))

    limit = 2
    print("GETTING latest ", limit, " rows from db: ")
    all_rows = getrecentfb_db(cursor, limit)
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns 2nd column (score)
        print('\t{0} : {1}: {2}'.format(row[3], row[1], row[2]))

    db.close()

if __name__ == '__main__':
    main()
