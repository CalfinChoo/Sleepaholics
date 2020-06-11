# Calvin Chu, Jeff Lin, Jackson Zou, Derek Leung - Team Sleepaholics
# SoftDev2 pd9
# P05 - Fin
# 2020-06-05

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from flask_socketio import SocketIO, send, join_room

import urllib.request, json
import os
import random
import string
from os import urandom

from db import *
from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(32)
socketio = SocketIO(app, cors_allowed_origins="*")
DB_FILE = "info.db"
init_db(DB_FILE)

@app.route("/")
def root():
    if "ign" in session:
        redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/home")
def home():
    print(session)
    if "ign" not in session: return redirect(url_for("login"))
    return render_template("home.html", ign = session["ign"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if len(request.form) != 0:
        result = checkUser(DB_FILE, request.form["username"], request.form["password"])
        if result:
            session["ign"] = result
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials")
            return redirect(url_for("login"))
    return render_template('login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if len(request.form) != 0:
        if (addUser(DB_FILE, request.form["username"], request.form["password"], request.form["password2"], request.form["ign"])):
            session["ign"] = request.form["ign"]
            return redirect(url_for("home"))
        else:
            flash("Passwords do not match or username is taken")
            return redirect(url_for("register"))
    return render_template('register.html')

@app.route("/create")
def create():
    dup = True
    room_id = ''
    while dup:
        for i in range(6):
            room_id+=random.choice(string.ascii_letters + string.digits)
        if checkroomid(DB_FILE, room_id):
            dup = False
    session["room_id"] = room_id
    createRoom(DB_FILE, room_id)
    return redirect(url_for("game"))

@app.route("/game", methods=["GET", "POST"])
def game():
    if len(request.form) != 0:
        # change lines below for room_id / password checker websocket thingy
        # if not match / does not exist, flash error and redirecct to home
        if findRoom(DB_FILE, request.form["room_id"]):
            return render_template("game.html", room_id = request.form["room_id"])
        return redirect(url_for("home"))
    return render_template('game.html', room_id = session["room_id"])

#logout route: removes the user from session and redirects to root
@app.route("/logout")
def logout():
    if "ign" in session:
        session.pop('ign')
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    socketio.run(app)
