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


conn.set_isolation_level(0) # set isolation level to modify tables, can't be in a transaction

cursor = conn.cursor()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS public.test (col1 varchar(50), col2 varchar(50) );""")
    cursor.execute("""INSERT INTO public.test  VALUES ('sam', 'jones'),('jane','smith')""")
except psycopg2.ProgrammingError as e:
    print "Issue with commands: ", e


