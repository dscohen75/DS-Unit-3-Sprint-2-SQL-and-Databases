import pandas as pd
import sqlite3
import psycopg2

tt = pd.read_csv('titanic.csv')

tt.to_sql('titanic_sqlite', )

dbname = "nizbvoyv"
user = "nizbvoyv"
password = "NqX4mdfsxyZV6ZDCQOuhwx3gaCPNAsW6" # This is sensitive; don't share or commit!
host = "topsy.db.elephantsql.com"

def connect_to_pg(dbname, user, 
    password, host, extraction_db=None):
    """ Connects to DB - return (sl_conn &) pg_conn """
    # sl_conn = sqlite3.connect(extraction_db) # local SQLite db
    pg_conn = psycopg2.connect(dbname=dbname, user=user, 
    password=password, host=host) # postgreSQL db
    return pg_conn

create_titanic_table = """
CREATE TYPE bernoulli AS ENUM ('0', '1');
CREATE TYPE sex AS ENUM ('male', 'female');
CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    survived BERNOULLI,
    pclass INT,
    name VARCHAR(40),
    sex SEX,
    age INT,
    sibs INT,
    parents INT,
    fare NUMERIC
)
"""

for person in tt_list:
    insert_person = """
        INSERT INTO titanic 
        (id, survived, pclass, name, sex, age, sibs, parents, fare)
        VALUES """ + str(tt_list[0] + ';'
    pg_curs.execute(insert_person)
    