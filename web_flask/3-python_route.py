#!/usr/bin/python3
"""
Script that starts Flask web application
Takes the following urls:
    '/'
    '/hbnb'
    '/c/<text>'
    '/python/(<text>)
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """displays 'C' followed by value of text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """
    Displays 'Python' followed by value of text variable
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


if __name__ == '__main__':
    """Start the flask web application"""
    app.run(host='0.0.0.0', port=5000)
