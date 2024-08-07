#!/usr/bin/env python3
"""Module Defining a simple Flask app
"""
from flask import Flask, render_template, request
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


@app.route('/', strict_slashes=False)
def index() -> str:
    """Return the app's index page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
