# Calvin Chu, Jeff Lin, Jackson Zou, Derek Leung - Team Sleepaholics
# SoftDev2 pd9
# P05 - Fin
# 2020-06-05

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
import urllib.request, json
import os
import random
import string
from os import urandom

from db import init_db, addUser, checkUser
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
    roomCode = ''
    for i in range(6):
        roomCode+=random.choice(string.ascii_letters + string.digits)
    return render_template('create.html', room_id=roomCode)

#logout route: removes the user from session and redirects to root
@app.route("/logout")
def logout():
    if "ign" in session:
        session.pop('ign')
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
