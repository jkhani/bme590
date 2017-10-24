from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello World %s" % name

@app.route("/data")
def data():
    a = {"temp": [20, 21, 21], "time": [10, 20, 30], "unit": "s"}
    arr = [a]
    return jsonify(arr)

@app.route("/add", methods=['POST'])
def add():
    value = request.json['a'] + request.json['b']
    return jsonify(value)
