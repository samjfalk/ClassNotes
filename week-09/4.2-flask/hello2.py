import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form['name']
        return greet(name)
    return render_template('index.html')

@app.route('/greet')
def greet(name):
    '''Say hello to your firts parameter'''
    return "Hello, %s!" %name

if __name__ == '__main__':
    app.run(debug=True)