# Calvin Chu, Jeff Lin, Jackson Zou, Derek Leung - Team Sleepaholics
# SoftDev2 pd9
# P05 - Fin
# 2020-06-05

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import urllib.request, json
import os
import random
from os import urandom

from db import init_db, addUser, checkUser, createRoom, checkroomid, findRoom
from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(32)
DB_FILE = "info.db"
init_db(DB_FILE)

@app.route("/")
def root():
    if "ign" in session:
        redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    print(session)
    if len(request.form) == 0:
        return render_template('login.html')
    result = checkUser(DB_FILE, request.form["username"], request.form["password"])
    if result:
        session["ign"] = result
        return redirect(url_for("home"))
    return render_template('login.html', errormessage = "invalid credentials")


@app.route("/register", methods=["GET", "POST"])
def register():
    print(session)
    if len(request.form) == 0:
        return render_template('register.html')
    if (addUser(DB_FILE, request.form["username"], request.form["password"], request.form["password2"], request.form["ign"])):
        session["ign"] = request.form["ign"]
        return redirect(url_for("home"))
    return render_template('register.html', errormessage = "passwords do not match or username is taken")

@app.route("/home", methods=["GET", "POST"])
def home():
    print(session)
    if len(request.form) == 0:
        return render_template("home.html", ign = session["ign"])
    if findRoom(DB_FILE, request.form["room_id"], request.form["password"]):
        return redirect("/game/{}".format(request.form["room_id"]))
    return render_template("home.html", errormessage = "Room not found or incorrect password")

@app.route("/create")
def create():
    set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    room_id = ""
    dup = True
    while dup:
        for i in range(8):
            room_id += random.choice(set)
        if checkroomid(DB_FILE, room_id):
            dup = False
    return render_template("create.html", room_id = room_id)

@app.route("/initroom/<room_id>", methods=["GET", 'POST'])
def initroom(room_id):
    createRoom(DB_FILE, room_id, request.form["password"])
    return redirect("/game/{}".format(room_id))

@app.route("/game/<room_id>")
def game(room_id):
    return render_template("game.html", room_id = room_id)

if __name__ == "__main__":
    app.debug = True
    app.run()
