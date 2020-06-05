# Calvin Chu, Jeff Lin, Jackson Zou, Derek Leung - Team Sleepaholics
# SoftDev2 pd9
# P05 - Fin
# 2020-06-05

from flask import Flask, render_template
import urllib.request, json

from pprint import pprint

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
