#!/usr/bin/python3
"""Flask app"""
from flask import render_template, url_for, redirect
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    """Flask app"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
