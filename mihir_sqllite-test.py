import sqlite3
from sqlite3 import Error

import datetime 
from datetime import datetime, date, timedelta

    # Get a cursor object
def createDB(db):
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT UNIQUE, 
    SoarScore FLOAT, CorrScore, udate DATE)''')
    db.commit()
    return cursor

# INITIALLIZE DB (called users) with 2 entries
def updateDB(db, name, Sscore, Cscore, udate):
    cursor = db.cursor()
    cursor.execute('''INSERT or REPLACE INTO users(name, SoarScore, CorrScore, udate)
                    VALUES(?,?,?,?)''', (name, Sscore, Cscore, udate))
    db.commit()
    return cursor

def updateToLatestDate(db):
    cursor = db.cursor()
    sdate = '2020-01-01'
    edate = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    all_rows = getPriorDB(cursor, sdate, edate)
    for row in all_rows:
        ticker = row[1]
        # fix this score to latest ticker
        SoarScore = '15'
        CorrScore = '20'
        today = datetime.strftime(datetime.now(), '%Y-%m-%d')
        updateDB(db, ticker, SoarScore, CorrScore, today)
        
    #SEARCH for MAX 
def getAllDB(cursor):
    cursor.execute('''SELECT name, SoarScore, CorrScore, udate FROM users''')
    all_rows = cursor.fetchall()
    return all_rows
    # for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns 2nd column (score)
    #     return print('{0} : {1}'.format(row[0], row[1]))

# UPDATE user with MAX score with new MAX score
def getMaxScoreDB(cursor, stype):
    if stype == 'Soar':
        cursor.execute('''SELECT max(SoarScore), CorrScore, name, udate FROM users''')
    elif stype == 'Corr':
        cursor.execute('''SELECT max(CorrScore), SoarScore, name, udate FROM users''')
    else:
        cursor.execute('''SELECT max(SoarScore), CorrScore, name, udate FROM users''') # Should be an error
    all_rows = cursor.fetchall()
    return all_rows
def getMinScoreDB(cursor, stype):
    if stype == 'Soar':
        cursor.execute('''SELECT min(SoarScore), CorrScore, name, udate FROM users''')
    elif stype == 'Corr':
        cursor.execute('''SELECT min(CorrScore), SoarScore, name, udate FROM users''')
    else:
        cursor.execute('''SELECT min(SoarScore), CorrScore, name, udate FROM users''') # Should be an error
    row = cursor.fetchone()
    return row

def getPriorDB(cursor, sdate, edate):
    cursor.execute('''SELECT * FROM users WHERE
    strftime('%s', udate) BETWEEN strftime('%s', ?) AND strftime('%s', ?)''', (sdate, edate))
    all_rows = cursor.fetchall()
    return all_rows

def main():
    #database = r"C:\Users\Arya\Desktop"
    database = r':memory:'

    # CREATE a database in file or RAM
    db = sqlite3.connect(database)

    cursor = createDB(db)

    name1 = 'AAPL'
    score1 = '1'
    score = '4'
    udate1 = datetime.strftime(datetime.now()-timedelta(3), '%Y-%m-%d')
    updateDB(db, name1, score1, score, udate1)

    name2 = 'GOOG'
    score2 = '4'
    score3 = '6'
    udate2 = datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')
    updateDB(db, name2, score2, score3, udate2)

    name3 = 'ZM'
    score3 = '7'
    score4 = '2'
    udate3 = date.today().strftime('%Y-%m-%d')
    updateDB(db, name3, score3, score4, udate3)

    print("GETTING ALL rows from db:")
    all_rows = getAllDB(cursor)
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns 2nd column (score)
        print('\t{0} : {1}: {2} : {3}'.format(row[0], row[1], row[2], row[3]))

    # UPDATE user with min score with new score
    row = getMinScoreDB(cursor, 'Corr')
    ticker = row[2]
    Sscore = row[1]
    newCscore = '9'
    newdate = datetime.strftime(datetime.now() - timedelta(5), '%Y-%m-%d')
    #updateDB(db, name, Sscore, Cscore, udate)
    updateDB(db, ticker, Sscore, newCscore, newdate)
    
    all_rows = getMaxScoreDB(cursor, 'Corr')
    print("RETRIEVING Max:")
    #print(all_rows)
    for row in all_rows:
    #    print(row)
        print('\t{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))


    #pdate = date.today().strftime('%Y-%m-%d')
    sdate = '2020-01-01'
    edate = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    all_rows = getPriorDB(cursor, sdate, edate)
    print("RETRIEVING Rows Prior to ", edate, ": ")
    #print(all_rows)
    for row in all_rows:
        print('\t{0} : {1} : {2} : {3}'.format(row[1], row[2], row[3], row[4]))
    
    updateToLatestDate(db)
    all_rows = getPriorDB(cursor, sdate, edate)
    print("RETRIEVING Rows Prior to ", edate, ": ")
    #print(all_rows)
    for row in all_rows:
        print('\t{0} : {1} : {2} : {3}'.format(row[1], row[2], row[3], row[4]))
    
    print("GETTING ALL rows from db:")
    all_rows = getAllDB(cursor)
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns 2nd column (score)
        print('\t{0} : {1}: {2} : {3}'.format(row[0], row[1], row[2], row[3]))
    db.close()

if __name__=="__main__":
    main()
