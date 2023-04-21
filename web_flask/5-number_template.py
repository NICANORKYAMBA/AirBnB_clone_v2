#!/usr/bin/python3
"""
Script that starts Flask web application

Take the following urls:
    '/'
    '/hbnb'
    '/c/<text>'
    '/python/(<text>)'
    '/number/<n>'
    '/number_template/<n>'
"""
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Displays 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Displays 'C' followed by the value of text variable
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """
    Displays 'Python' followed by the value of text
    variable
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Displays n followed by 'is number' of n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """
    Displays HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """Start Flask web application"""
    app.run(host='0.0.0.0', port=5000)
