from flask import Flask,request, jsonify,g
import sqlite3
app = Flask(__name__)

DATABASE = 'student.db'

@app.route('/',methods = ['GET'])
def index():
    return jsonify ({'msg':'hello world'})


if __name__ == '__main__':
    app.run(debug = True)