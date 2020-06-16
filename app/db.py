import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
import urllib.request as urllib2
import json

def init_db(DB_FILE):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS USER(username TEXT, password TEXT, ign TEXT, room_id TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS GAMES(room_code TEXT);")
    c.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='WORDS' ")
    if c.fetchone()[0] < 1:
        c.execute('CREATE TABLE WORDS(word TEXT);')
        thing = urllib2.urlopen("https://random-word-api.herokuapp.com/all")
        thing2 = thing.read()
        thing3 = json.loads(thing2)
        for x in thing3:
            c.execute('INSERT INTO WORDS VALUES (?)', (x,))
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
        c.execute("INSERT INTO USER VALUES(\"{}\", \"{}\", \"{}\", {});".format(username, generate_password_hash(password), ign, "NULL"))
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

def createRoom(DB_FILE, room_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO GAMES VALUES(\"{}\");".format(room_id))
    db.commit()
    db.close()
    return True

def getRoomPlayers(DB_FILE, room_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT ign FROM USER WHERE room_id = \"{}\";".format(room_id))
    players = []
    for item in c.fetchall():
        players.append(item[0])
    db.close()
    return players

def getWords(DB_FILE):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM WORDS")
    words = []
    for w in c.fetchall():
        words.append(w[0])
    db.close()
    return words

def updateRoomExistence(DB_FILE):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT room_code FROM GAMES;")
    q = c.fetchall()
    for item in q:
        c.execute("SELECT * FROM USER WHERE room_id = \"{}\";".format(item[0]))
        if not len(c.fetchall()):
            print("DELETING {}".format(item[0]))
            c.execute("DELETE FROM GAMES WHERE room_code = \"{}\";".format(item[0]))
    db.commit()
    db.close()
    return True

def updateUserRoom(DB_FILE, ign, room_id=None, leaving=False):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if leaving:
        c.execute("UPDATE USER SET room_id = NULL WHERE ign = \"{}\";".format(ign))
    else:
        c.execute("UPDATE USER SET room_id = \"{}\" WHERE ign = \"{}\";".format(room_id,ign))
    db.commit()
    db.close()
    return True

def findRoom(DB_FILE, room_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM GAMES WHERE room_code = \"{}\";".format(room_id))
    q = c.fetchall()
    if len(q) == 0:
        return False
    db.close()
    return True
