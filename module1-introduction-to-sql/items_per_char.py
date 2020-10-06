import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# How many items does each character have?
# Return first 20 rows

ITEMS_BY_CHAR = """
SELECT cci.character_id, cc.name, COUNT(*)
FROM charactercreator_character_inventory AS cci, 
charactercreator_character AS cc
WHERE cci.character_id = cc.character_id
GROUP BY cci.character_id
LIMIT 20;
"""

# How many items does each character have ON AVERAGE?

AVG_ITEMS = """
SELECT AVG(num_items) FROM
(SELECT cci.character_id, cc.name, COUNT(*) AS num_items
FROM charactercreator_character_inventory AS cci, 
charactercreator_character AS cc
WHERE cci.character_id = cc.character_id
GROUP BY cci.character_id);
"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results1 = execute_query(curs, ITEMS_BY_CHAR)
    print(results1)
    curs = conn.cursor()
    results2 = execute_query(curs, AVG_ITEMS)
    print(results2)