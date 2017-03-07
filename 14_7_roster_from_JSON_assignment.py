import json
import sqlite3
import os

dir = os.path.dirname(__file__)
db_path = os.path.join(dir, 'SQLite/courseraRoster.sqlite')


conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Drop existing and create new tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file_path = os.path.join(dir, 'files/roster_data.json')

# Example entry of the file:
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(file_path).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print name, title

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''', (user_id, course_id, role))

conn.commit()
