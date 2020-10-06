import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# How many weapons does each character have?
# Return first 20 rows

WEAPONS_BY_CHAR = """
SELECT character_id, item_ptr_id, COUNT(*)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id
LIMIT 20;
"""

# How many weapons does each character have ON AVERAGE?

AVG_WEAPONS = """
SELECT AVG(items) FROM
(SELECT COUNT(DISTINCT character_id) AS items
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON item_id = item_ptr_id);
"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results1 = execute_query(curs, WEAPONS_BY_CHAR)
    print(results1)
    curs = conn.cursor()
    results2 = execute_query(curs, AVG_WEAPONS)
    print(results2)