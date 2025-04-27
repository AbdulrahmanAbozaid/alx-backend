#!/usr/bin/env python3
"""Minimal app"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)


@app.route('/')
def hello():
    """Main entry"""
    return render_template('0-index.html')
