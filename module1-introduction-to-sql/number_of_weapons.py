import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

NUM_WEAPONS = """
SELECT COUNT(item_id) 
FROM armory_item, armory_weapon
WHERE item_id = item_ptr_id;
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, NUM_WEAPONS)
    print(results, ' of the items are weapons.')