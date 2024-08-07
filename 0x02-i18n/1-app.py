#!/usr/bin/env python3
"""Module Defining a simple Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """class for configuring the flask app
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
# app.config.from_object(Config())
babel = Babel(app, default_locale=Config.LANGUAGES[0], default_timezone='UTC')


@app.route('/', strict_slashes=False)
def index() -> str:
    """Return the app's index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
