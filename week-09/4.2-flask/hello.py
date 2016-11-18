import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "<h2>Hello World!</h2>"

@app.route('/greet/<name>')
def greet(name):
    '''say hello to your first parameter'''
    return 'hello, %s' %name

if __name__ == '__main__':
    app.run(debug=True)