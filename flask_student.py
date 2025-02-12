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

# students
@app.route('/students', methods = ['GET'])
def get_all_students():
    db = get_db()
    students = db.execute('SELECT * from students').fetchall()
    return jsonify({'students':students})

#add students

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
    


#update students

@app.route('/update-student/<int:id>',methods = ['PUT'])
def update_student():
    data = request.json
    
    if  'name' in data.keys() and data['name'].strip() == '':
        return jsonify({'error':'name firld cannot be empty'}), 400
    if  'class' in data.keys() and data['class'].strip() == '':
        return jsonify({'error':'class firld cannot be empty'}), 400
    
    db = get_db()
    if 'name' in data.keys():
        db.execute('UPDATE students SET name = ? where id = ?', [data['name'],id])
    if 'class' in data.keys():
        db.execute('UPDATE students SET class = ? where id = ?', [data['class'],id])

#delete student

@app.route('/delete-student/<int:id>',methods = ['DELETE'])
def delete_student(id):
    db = get_db()
    db.execute('DELETE FROM students WHERE id = ?',[id])
    db.commit()
    return jsonify({'message',f'student {id} deleted sucessfuly'})

#get student by id

@app.route('/student/<int:id>',methods = ['GET'])
def get_student(id):
    db = get_db()
    student = db.execute('SELECT * FROM students WHERE id = ?',[id].featchone())
    if student is None:
        return jsonify({'msg':'no id found'})

if __name__ == '__main__':
    app.run(debug = True)