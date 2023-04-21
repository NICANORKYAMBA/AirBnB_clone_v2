#!/usr/bin/python3
"""
Script that starts Flask web application

Takes the following urls:
    '/'
    '/hbnb'
    '/c/<text>'
    '/python/(<text>)'
    '/number/<n>'
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
    """
    Displays 'C' followed by value of the text variable
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_c_python(text='is cool'):
    """
    Displays 'Python' followed by the value of optional
    text variable which is set to default 'is cool' value
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Displays n if only it's an integer
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    """starts the flask web application"""
    app.run(host='0.0.0.0', port=5000)
