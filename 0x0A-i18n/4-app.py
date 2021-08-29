#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
""" App Flask """
babel = Babel(app)
""" Babel, TIME zone/Locale """


class Config(object):
    """ class configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" make this class as config default for Flask application """


@app.route("/")
def index():
    """Flask app"""
    return render_template('1-index.html')


@babel.localeselector
def get_locale(methods=['POST', 'GET']):
    """ best match with our supported languages """
    local_language = request.args.get('locale')
    language_support = app.config['LANGUAGES']
    if local_language in language_support:
        return local_language
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
