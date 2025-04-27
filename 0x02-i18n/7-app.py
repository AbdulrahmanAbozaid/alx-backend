#!/usr/bin/env python3
"""Minimal app"""
from email.utils import format_datetime
from flask import Flask, request, render_template, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Store the app configs"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """returns a user dictionary"""
    print(request.args.get("login_as"))
    if not request.args.get("login_as"):
        return None
    return users.get(int(request.args.get("login_as")), None)


@app.before_request
def before_request():
    """use get_user to find a user if any, and set it as a global on g.user."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Get the best locale"""
    return (
        request.args.get("locale")
        or (
            g.get("user")
            and (
                g.get("user").get("locale") in Config.LANGUAGES
                and g.get("user").get("locale")
            )
        )
        or request.accept_languages.best_match(Config.LANGUAGES)
    )


@babel.timezoneselector
def get_timezone() -> str:
    """Get the time zone"""
    user = getattr(g, "user", None)
    try:
        return request.args.get("timezone") or (
            user and pytz.timezone(user.get("timezone"))
        )
    except pytz.exceptions.UnknownTimeZoneError:
        return "UTC"


@app.route("/")
def hello():
    """Main entry"""
    return render_template("7-index.html", current_time=format_datetime(datetime.now()))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
