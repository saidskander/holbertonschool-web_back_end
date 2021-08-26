#!/usr/bin/python3
"""Flask app"""
from flask import render_template
from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)
""" Babel, TIME zone/Locale """


class Config(object):
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Use that class as config for Flask app """


@app.route("/")
def rout():
    """Flask app"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
