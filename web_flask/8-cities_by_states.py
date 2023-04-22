#!/usr/bin/python3
"""Script that starts Flask web application

Takes:
    '/cities_by_states'
"""
from flask import Flask
from flask import render_template
from models import storage, State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_and_cities():
    """
    Displays HTML page
    """
    states = storage.all(State)

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage connection after each request
    """
    storage.close()


if __name__ == '__main__':
    """Starts Flask web application"""
    app.run(host='0.0.0.0', port=5000)
