# Calvin Chu, Jeff Lin, Jackson Zou, Derek Leung - Team Sleepaholics
# SoftDev2 pd9
# P05 - Fin
# 2020-06-05

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import urllib.request, json
import os
from os import urandom

from db import init_db
from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(32)
DB_FILE = "info.db"
init_db(DB_FILE)


@app.route("/")
def root():
    if ('ign' in session):
        redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/home")
def home():
    return render_template("home.html", ign = session["ign"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if len(request.form) == 0:
        return render_template('login.html')
    session["ign"] = request.form["username"]
    return redirect(url_for("home"))


@app.route("/register")
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
