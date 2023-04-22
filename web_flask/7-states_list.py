#!/usr/bin/python3
"""
Script that starts Flask web applicatiob

Takes the following routes:
    '/states_list'
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all State objects"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage connection after each request"""
    storage.close()


if __name__ == '__main__':
    """Start flask web application"""
    app.run(host='0.0.0.0', port=5000)
