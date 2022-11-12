#!/usr/bin/python3
from flask import Flask, escape, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    return("HBNB")


@app.route('/c/<text>')
def c_dynamic(text):
    
    text = text.replace('_', ' ')
    return("C %s" % escape(text))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_dynamic(text):
    
    text = text.replace('_', ' ')
    return("Python %s" % escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
