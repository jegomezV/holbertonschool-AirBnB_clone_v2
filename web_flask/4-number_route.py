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
    '/': Return: "Hello HBNB"
    '/hbnb': Return: "HBNB"
    '/c/<text>': Return: "C + <text>"
    '/python/<text>': Return: "Python + <text>", default text="is cool"
    '/number/<n>': Return: "<n> is a number", only if is a number
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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Funtion that return string using "<text>"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Funtion that return string using "<text>, default=is cool"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """Return a text if is a int"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
