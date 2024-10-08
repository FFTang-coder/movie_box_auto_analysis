from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1> Welcome to my world!<img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user(name):
    return f'Hello, {escape(name)}!'


@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('user', name='germey'))
    print(url_for('test_url_for', num=2))
    return 'Test page'