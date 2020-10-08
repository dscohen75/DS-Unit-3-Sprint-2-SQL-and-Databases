import pymongo
import sqlite3

password = 'wHZjnE2MwDZrFgjc'
dbname = 'test'

def create_mdb_connection(password, dbname):
    # Using string formatting to put in password and dbname 
    client = pymongo.MongoClient(
        "mongodb+srv://debbiecohen:{}@cluster0.dyh6m.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname))
    return client

def create_sl_connection(extraction_db="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db) 
    return sl_conn

def execute_query(curs, query):
    return curs.execute(query).fetchall()

def show_sl_schema(table):
    schema = "PRAGMA table_info(" + table + "):"

# Could use the above function to figure out how to make this more robust
# How to do this also with insert_many()?

def character_doc_creation(db, character_table):
    for character in character_table:
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8]
        }
        db.insert_one(character_doc)

def show_all(db):
    all_docs = list(db.find())
    return all_docs

# SQLite queries

get_characters = "SELECT * FROM charactercreator_character"


if __name__ == "__main__":
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(password, dbname)
    db = client.test
    # Now return the contents of the characters table as a list of tuples
    characters = execute_query(sl_curs, get_characters)
    character_doc_creation(db.test, characters)
    print(show_all(db.test))
    
