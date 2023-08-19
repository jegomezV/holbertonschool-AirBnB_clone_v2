#!/usr/bin/python3
"""
Module Name:
0-hello_route

Module Description:
This module contains the routers

Module Attributes:
- None
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
