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
    '/number_template/<n>': Return a HTML struct if n is int
    '/number_odd_or_even/<n>': Return a HTML struct is n is int and if is even
                                or if is odd.
'''
from flask import Flask, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Return a HTML template if n is a int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """ Return a HTML template if n is a int"""
    if n % 2 == 0:
        type_n = "even"
    else:
        type_n = "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_even=type_n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
