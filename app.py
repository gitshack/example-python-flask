from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is the <b>Home</b> Page</h1><p><a href="/">Home</a></p><p><a href="/about">About</a></p>'

@app.route('/about')
def hello():
    return '<h1>This is the <b>About</b> Page</h1><p><a href="/">Home</a></p><p><a href="/about">About</a></p>'
