import pandas as pd
import sqlite3
import psycopg2

tt = pd.read_csv('titanic.csv')

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

def execute_query(curs, query):
    return curs.execute(query)
    

tt_list = [tuple(r) for r in tt.to_numpy()] 
print("tt_list[0:5]", tt_list[0:5])   # Sanity check

# Only had to run this once to create the type
create_type_sex = """
CREATE TYPE sex AS ENUM ('male', 'female');
"""

create_titanic_table = """
CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex SEX,
    age INT,
    sibs INT,
    parents INT,
    fare NUMERIC
)
"""

# print("str(tt_list[0][1:])", str(tt_list[0][1:]))  # Sanity check

example_insert = """
INSERT INTO titanic
(survived, pclass, name, sex, age, sibs, parents, fare)
VALUES """ + str(tt_list[0]) + ';'

check_postgres_titanic_exists = "SELECT * FROM titanic"

if __name__ == '__main__':
    pg_conn = connect_to_pg(dbname, user, password, host)
    pg_curs = pg_conn.cursor()
    execute_query(pg_curs, create_type_sex)
    execute_query(pg_curs, create_titanic_table)
    for person in tt_list[0:10]:
        person_l = list(person)
        person_l[2] = person_l[2].replace("'","")
     #   print('person_l =', person_l)
        person = tuple(person_l)
     #   print("person = ", person)
        insert_person = """
            INSERT INTO titanic 
            (survived, pclass, name, sex, age, sibs, parents, fare)
            VALUES """ + str(person) + ';'
        pg_curs.execute(insert_person)
    result = execute_query(pg_curs, check_postgres_titanic_exists)
    print(result)
    pg_conn.commit()


