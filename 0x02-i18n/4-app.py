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


@babel.localeselector
def get_locale():
    """Get the best locale"""
    return request.args.get("locale") or request.accept_languages.best_match(
        ["en", "fr"]
    )


@app.route("/")
def hello():
    """Main entry"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
