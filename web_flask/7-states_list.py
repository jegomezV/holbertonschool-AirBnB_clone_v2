#!/usr/bin/python3
'''
MODULE NAME:
------------
    7-states_list.py

MODULE DESCRIPTION:
-------------------
    That return a HTML with the States shorted

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


@app.route('/states_list', strict_slashes=False)
def state_list():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
