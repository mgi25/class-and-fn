from flask import Flask,request, jsonify,g
import sqlite3
app = Flask(__name__)

DATABASE = 'students.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


with app.app_context():   #this part of the code will start work when the falsk app start working 
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS students\
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, class TEXT)')
    db.commit()
    

@app.route('/',methods = ['GET'])
def index():
    return jsonify ({'msg':'hello world'})


@app.route('/students', methods = ['GET'])
def get_all_students():
    db = get_db()
    students = db.execute('SELECT * from students').fetchall()
    return jsonify({'students':students})

@app.route('/add-student',methods = ['POST'])
def add_student():
    data = request.json
    if  'name' and 'class' not in data.keys():
        return jsonify({'error': 'NAME and CLASS fields are reqired'}), 400
    
    if data['name'].strip() == '' or data['class'].strip() == '':
        return jsonify({'error':'name and class fields cannot be empty'}), 400
    
    db = get_db()
    db.execute('INSERT INTO students (name,class) VALUES (?,?)',
               [data['name'],data['class']])
    db.commit()
    
    return jsonify({'message':f'student {data['name']} added succesfully'}), 201
    

if __name__ == '__main__':
    app.run(debug = True)