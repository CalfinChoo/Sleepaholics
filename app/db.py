import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

def init_db(DB_FILE):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS USER(username TEXT, password TEXT, ign TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS GAMES(room_code TEXT, password TEXT, player_count INTEGER);")
    db.commit()
    db.close()

def addUser(DB_FILE, username, password, password2, ign):
    if password != password2:
        return False
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM USER WHERE username = \"{}\";".format(username))
    q = c.fetchall()

    if len(q) == 0:
        c.execute("INSERT INTO USER VALUES(\"{}\", \"{}\", \"{}\");".format(username, generate_password_hash(password), ign))
        db.commit()
        db.close()
        return True
    return False

def checkUser(DB_FILE, username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM USER WHERE username = \"{}\";".format(username))
    q = c.fetchall()
    if len(q) == 0:
        return False
    if check_password_hash(q[0][1], password):
        return q[0][2]
    return False

def checkroomid(DB_FILE, room_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM GAMES WHERE room_code = \"{}\";".format(room_id))
    q = c.fetchall()
    db.close()
    if len(q) == 0:
        return True
    return False

def createRoom(DB_FILE, room_id, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO GAMES VALUES(\"{}\", \"{}\", 1);".format(room_id, generate_password_hash(password)))
    db.commit()
    db.close()
    return True

def findRoom(DB_FILE, room_id, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM GAMES WHERE room_code = \"{}\";".format(room_id))
    q = c.fetchall()
    if len(q) == 0:
        return False
    if check_password_hash(q[0][1], password):
        playercount = q[0][2] + 1
        c.execute("UPDATE GAMES SET player_count = {} WHERE room_code = \"{}\"".format(playercount, room_id))
        db.commit()
        db.close()
        return True
    return False
