#!/usr/bin/python3
from flask import render_template, url_for, redirect
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
