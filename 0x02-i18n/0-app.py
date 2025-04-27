#!/usr/bin/env python3
"""Minimal app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    """Main entry"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
