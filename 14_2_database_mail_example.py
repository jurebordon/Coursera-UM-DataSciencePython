import sqlite3
import os

dir = os.path.dirname(__file__)
db_path = os.path.join(dir, 'SQLite/firstDatabase.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

file_path = os.path.join(dir, 'files/mbox-short.txt')
fhandler = open(file_path)

for line in fhandler:
    if not line.startswith("From: "):
        continue

    pieces = line.split()
    email = pieces[1]

    # Single tuple (email, ), weird sintax, but has to be like that
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count = count+1 WHERE email= ? ', (email, ))
    except:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email, ))


conn.commit()
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
