import sqlite3
import psycopg2

# Step 1, extract: get data out of SQLite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

GET_CHARACTERS = "SELECT * FROM charactercreator_character;"

sl_curs.execute(GET_CHARACTERS)

characters = sl_curs.fetchall()

# Step 1 complete - we have a list of tuples with all character data
# Note this is not a pandas df
# We don't know types, so for Transform we need to figure that out
# because our destination (PostgreSQL) needs a schema for this data

# Step 2 -Transform
# Make a schema to define a table that fits these data in PostgreSQL
# This is an internal meta sort of query, will vary by database flavor

sl_curs.execute('PRAGMA table_info(charactercreator_character);')
sl_curs.fetchall()


# Make a connection to the PostgreSQL database
dbname = "nizbvoyv"
user = "nizbvoyv"
password = "NqX4mdfsxyZV6ZDCQOuhwx3gaCPNAsW6" # This is sensitive; don't share or commit!
host = "topsy.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, 
                           user=user, 
                           password=password, 
                           host=host)

pg_curs = pg_conn.cursor() # works the same as SQLite

# Make a PostgreSQL CREATE statement that captures the schema of the SQLite db
create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""

# Excute the CREATE TABLE statement
pg_curs.execute(create_character_table)
pg_conn.commit()

# Insert all of the characters data into the new PostgreSQL db
for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)
    ## This does the inserting one at a time
    ## As a stretch, try to combine into a single INSERT statement

pg_conn.commit()

## Check systematically that the data are all the same
pg_curs.execute('SELECT * FROM charactercreator_character')
pg_characters = pg_curs.fetchall()

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

## close the cursors and connections

pg_cursor.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()
