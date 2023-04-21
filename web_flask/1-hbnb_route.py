#!/usr/bin/python3
"""script that starts Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    """starting flask web applictaion"""
    app.run(host='0.0.0.0', port=5000)
