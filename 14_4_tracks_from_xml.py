import xml.etree.ElementTree as ET
import sqlite3
import os

dir = os.path.dirname(__file__)
db_path = os.path.join(dir, 'SQLite/musicApp.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Drop existing and create new using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

file_path = os.path.join(dir, 'files/Library.xml')

# The function lookup goes through the 'leaf' dict entry and checks
# if the 'key' we are looking for is inside that entry. If it is
# retrieve the text of the next child (next interation of for)
#
# Example from the file:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


xml_file = ET.parse(file_path)
all = xml_file.findall('dict/dict/dict')
print 'Number of tacks:', len(all)
for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print name, artist, album, count, rating, length

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''', (name, album_id, length, rating, count))

    conn.commit()
