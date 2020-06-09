# Calvin Chu, Jeff Lin, Jackson Zou, Derek Leung - Team Sleepaholics
# SoftDev2 pd9
# P05 - Fin
# 2020-06-05

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import urllib.request, json
import os
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
    return render_template("home.html", ign = session["ign"])

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



if __name__ == "__main__":
    app.debug = True
    app.run()
