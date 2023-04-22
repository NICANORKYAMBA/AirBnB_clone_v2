#!/usr/bin/python3
"""
Module for a Flask web application to manage states and cities.
"""

from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database at the end of the request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a list of all the states."""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_cities_list(id):
    """Displays a list of all the cities in a state."""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    """Start Flask web application"""
    app.run(host='0.0.0.0', port=5000)
