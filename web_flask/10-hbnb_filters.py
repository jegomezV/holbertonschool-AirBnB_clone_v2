#!/usr/bin/python3
'''
MODULE NAME:
------------
    10-hbnb_filters

MODULE DESCRIPTION:
-------------------
    That return a HTML with the states, cities and amenities

MODULE ATTRUBUTES:
------------------
    None

ROUTES:
-------
    '/hbnb_filters' Return a HTML
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def state_list(id=None):
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
