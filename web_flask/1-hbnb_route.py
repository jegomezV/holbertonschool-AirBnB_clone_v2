#!/usr/bin/python3

'''
MODULE NAME:
------------
    0-hello_route

MODULE DESCRIPTION:
-------------------
    That starts a Flask web application

MODULE ATTRIBUTES:
------------------
    None

ROUTES:
-------
    '/': Return: "Hello HBNB"flask
    '/hbnb': Return: "HBNB"
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Funtion that return a string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Funtion that return a string"""
    return ("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
