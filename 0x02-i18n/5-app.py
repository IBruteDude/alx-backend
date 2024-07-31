#!/usr/bin/env python3
"""Module Defining a simple Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional


class Config:
    """class for configuring the flask app
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, default_locale=Config.LANGUAGES[0], default_timezone='UTC')


@babel.localeselector
def get_locale() -> Optional[str]:
    """get the best matching locale from configured languages
    """
    if request.args.get('locale', None) in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    if user_id is None:
        return None
    user_id = int(user_id)
    return users.get(user_id, None)


@app.before_request
def before_request():
    user_id = request.args.get('login_as', None)
    user = get_user(user_id)
    if user is not None:
        g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """Return the app's index page
    """
    return render_template('5-index.html',
                           logged_in=(getattr(g, 'user', False)))


if __name__ == '__main__':
    app.run(debug=True)
