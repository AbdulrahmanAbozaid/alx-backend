#!/usr/bin/env python3
"""Minimal app"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """Store the app configs"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """Get the best locale"""
    return request.args.get("locale") or request.accept_languages.best_match(
        ["en", "ar"]
    )


@app.route("/")
def hello():
    """Main entry"""
    return render_template("0-index.html")
