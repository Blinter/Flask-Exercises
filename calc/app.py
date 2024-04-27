from flask import Flask
from flask import request
import operations


app = Flask(__name__)

@app.route("/add")
def add():
    """Adds a and b"""
    return str(operations.add(int(request.args["a"]), int(request.args["b"])))

@app.route("/sub")
def sub():
    """Subtract a and b"""
    return str(operations.sub(int(request.args["a"]), int(request.args["b"])))

@app.route("/mult")
def mult():
    """Multiply a and b"""
    return str(operations.mult(int(request.args["a"]), int(request.args["b"])))

@app.route("/div")
def div():
    """Divide a and b"""
    return str(operations.div(int(request.args["a"]), int(request.args["b"])))

@app.route("/math/<operation>")
def aio(operation):
    """Combines 4 math functions as one query"""
    return {
        'add': add(),
        'sub': sub(),
        'mult': mult(),
        'div': div()
    }[operation]
