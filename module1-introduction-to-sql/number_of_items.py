import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# How many total items are there?

NUM_ITEMS = """
SELECT COUNT(DISTINCT item_id) 
FROM charactercreator_character_inventory;
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, NUM_ITEMS)
    print('There are ', results, 'total items.')