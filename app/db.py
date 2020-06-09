import sqlite3

def init_db(DB_FILE):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' ''')
    if c.fetchone()[0] < 1:
        c.execute("CREATE TABLE USER(username TEXT, password TEXT, ign TEXT);")
        c.execute("CREATE TABLE GAMES(room_code TEXT, password TEXT, player_count INTEGER);")
    db.commit()
    db.close()
