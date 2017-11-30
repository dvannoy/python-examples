#!usr/bin/env python
"""
    Based on tutorial found at https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
"""

import psycopg2
from config import POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

host = POSTGRES_HOST
user = POSTGRES_USER
password = POSTGRES_PASSWORD
db = POSTGRES_DB

try: 
    conn = psycopg2.connect("dbname='{0}' host='{1}' user='{2}' password='{3}'".format(db, host, user, password))
except Exception as e:
    print "Error connecting to database", e

cursor = conn.cursor()

cursor.execute("""SELECT * FROM public.test""")
results = cursor.fetchall()

for row in results:
    print row[0], row[1]

