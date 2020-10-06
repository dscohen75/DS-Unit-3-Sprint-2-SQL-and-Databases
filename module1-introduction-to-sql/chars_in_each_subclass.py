import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

NUM_CLERICS = """
SELECT COUNT(*)
FROM charactercreator_cleric;
"""

NUM_FIGHTERS = """
SELECT COUNT(*)
FROM charactercreator_fighter;
"""

NUM_MAGES = """
SELECT COUNT(*)
FROM charactercreator_mage;
"""

NUM_NECROS = """
SELECT COUNT(*)
FROM charactercreator_necromancer;
"""

NUM_THIEVES = """
SELECT COUNT(*)
FROM charactercreator_thief;
"""

queries = list([NUM_CLERICS, NUM_FIGHTERS, NUM_MAGES, 
                NUM_NECROS, NUM_THIEVES])

subclasses = ['clerics','fighters','mages','necromancers','thieves']

if __name__ == '__main__':
    i = 0
    for subclass in subclasses:
        conn = connect_to_db()
        curs = conn.cursor()
        results = execute_query(curs, queries[i])
        print('Number of ', subclasses[i], ': ' , results)
        i += 1