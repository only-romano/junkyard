import sqlite3 as sql

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sql.connect('files/test.db')
curs = conn.cursor()

curs.execute("""
CREATE TABLE food (
  id        TEXT    PRIMARY KEY,
  desc      TEXT,
  water     FLOAT,
  kcal      FLOAT,
  protein   FLOAT,
  fat       FLOAT,
  ash       FLOAT,
  carbs     FLOAT,
  fiber     FLOAT,
  sugar     FLOAT
)
""")

field_count = 10
markers = ', '.join(['?']*field_count)
query = 'INSERT INTO food VALUES (%s)' % markers

for line in open('files/abbrev.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()
