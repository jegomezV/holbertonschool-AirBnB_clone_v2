#!/usr/bin/python3
'''
MODULE NAME:
------------
    8-cities_by_states.py

MODULE DESCRIPTION:
-------------------
    That return a HTML with the cities by states

MODULE ATTRUBUTES:
------------------
    None

ROUTES:
-------
    '/states_list' Return a HTML template by all states
'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
