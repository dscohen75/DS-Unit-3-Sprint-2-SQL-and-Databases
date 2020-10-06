import pandas as pd
import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Load in the data set
bh = pd.read_csv('buddymove_holidayiq.csv')
bh['User_Id'] = bh['User Id']
bh = bh.drop('User Id', axis=1)

# Create a connection to a new blank database file 'buddymove_holidayiq.sqlite3'
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Insert the data into a new table called review in 'buddymove_holidayiq.sqlite3'
bh.to_sql('review', conn)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# How many users reviewed at least 100 in the nature catergory
# as well as at least 100 in the shopping category?

HINAT_HISHOP = """
SELECT COUNT(*)
FROM review
WHERE Nature >99 AND Shopping >99
"""

if __name__ == '__main__':
    curs = conn.cursor()
    results = execute_query(curs, HINAT_HISHOP)
    print(results)