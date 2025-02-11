from flask import Flask,jsonify,request, g
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db' # defining the database names


# setting up db
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# executing the query
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# closing the connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
with app.app_context():
    db=get_db()
    db.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, dob TEXT, address TEXT, phone TEXT, email TEXT)")
    db.commit()

@app.route('/students',methods = ["GET"])
def get_students():
    query_db('insert into students (name,dob,address,phone,email) values (?,?,?,?,?)',['Alen','1990-01-01','123 Main St','123-456-7890','alenjinmgi@gmail.com'])
    students = query_db('select * from students')
    return jsonify({'students':students})

@app.route('/',methods = ["GET"])
def return_hello():
    cur = get_db().cursor()
    return jsonify({'msg':'Hello'})


if __name__ == '__main__':
    app.run(debug=True)