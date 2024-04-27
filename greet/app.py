from flask import Flask


app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """Returns welcome"""


    html = "<html><body><h1>welcome</h1></body></html>"
    return html


@app.route('/welcome/home')
def welcome_home():
    """Returns welcome home"""


    html = "<html><body><h1>welcome home</h1></body></html>"
    return html


@app.route('/welcome/back')
def welcome_back():
    """Returns welcome back"""


    html = "<html><body><h1>welcome back</h1></body></html>"
    return html