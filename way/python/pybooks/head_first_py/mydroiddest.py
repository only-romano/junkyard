import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE athletes (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    dob DATE NOT NULL )""")

cursor.execute("""CREATE TABLE timing_data (
    athlete_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (athlete_id) REFERENCES athletes )""")

connection.commit()

import glob
import athletemodel

data_files = ['james', 'julie', 'mikey', 'sarah']
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].birth

    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    connection.commit()

connection.close()
