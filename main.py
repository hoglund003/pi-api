import os
import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome!"

@app.route('/add')
def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    aws = num1 + num2

    return jsonify(aws)

@app.route('/run')
def run():
    try:
        script = request.args.get('script')
    except Exception:
        return jsonify('No script given')
    
    try:
        os.system(f"python3 scripts/{script}")
    except Exception:
        return jsonify('No script found')

    return jsonify('response: {200}')

app.run()