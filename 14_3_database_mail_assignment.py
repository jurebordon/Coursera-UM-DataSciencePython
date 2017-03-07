import sqlite3
import os

dir = os.path.dirname(__file__)
db_path = os.path.join(dir, 'SQLite/firstDatabase.db')

path = db_path

conn = sqlite3.connect(path)
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

file_path = os.path.join(dir, 'files/mbox-short.txt')
fhandler = open(file_path)

for line in fhandler:
    if not line.startswith("From: "):
        continue

    pieces = line.split()
    email = pieces[1]
    organization = email.split('@')[1]

    # Single tuple (org, ), weird sintax, but has to be like that
    cur.execute('SELECT count FROM Counts WHERE org = ?', (organization, ))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count = count+1 WHERE org= ? ', (organization, ))
    except:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (organization, ))


conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
