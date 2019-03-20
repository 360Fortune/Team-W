# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:25:42 2019

@author: Patrick Peters
"""

import psycopg2 as pg
"""
datei = open(".\MasterCLass\Wetterstationen\Ergebnis\Station.csv", 'r')
datei.readline()

li = []
la = []

for i in datei:
    i = i.strip("\n").split(';')
    li.append((i[2], i[1]))
    # li.append((str(i[0]),str(i[2]),str(i[1])))
    la.append((str(i[0]),str(i[4]),str(i[3]),str(i[5])))

print(li)
"""

#Verbindung zur Datenbank (DB)
db = pg.connect(
        host = 'localhost',
        port = '5432',
        dbname = "Wetter",
        user = "postgres",
        password = "PyPostgres"
    )

#Cursor erstellen für die Kommunikation mit der DB
cursor = db.cursor()
# gibt alle ordner zurück
cursor.execute("SELECT * FROM pg_catalog.pg_tables")

for i in cursor:
    print(i)

# fügt in eine liste ein
# print(li[0])
sql = "INSERT INTO stationsname (id, stationsname) VALUES (%s, %s)"
val = [
        ("7", "Testberg"),
        ("8", "Teteat")
    ]
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")