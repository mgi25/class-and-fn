from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)

DATABASE = 'students.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


with app.app_context():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS students\
                (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, class TEXT)')
    db.commit()


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})


@app.route('/students', methods=['GET'])
def get_all_students():
    db = get_db()
    students = db.execute('SELECT * FROM students').fetchall()
    return jsonify({'students': students})


@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json

    if 'name' and 'class' not in data.keys():
        return jsonify({'error': 'name and class fields are required'}), 400

    if data['name'].strip() == '' or data['class'].strip() == '':
        return jsonify({'error': 'name and class fields cannot be empty'}), 400

    db = get_db()
    db.execute('INSERT INTO students (name, class) VALUES (?,?)',
               [data['name'], data['class']])
    db.commit()

    return jsonify({'message': f'Student {data['name']} added successfully'}), 201


@app.route('/update-student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
  
    if not 'name' in data.keys() and not 'class' in data.keys():
        return jsonify({'error': 'name or class field is required'}), 400

    if 'name' in data.keys() and data['name'].strip() == '':
        return jsonify({'error': 'name field cannot be empty'}), 400
    
    if 'class' in data.keys() and data['class'].strip() == '':
        return jsonify({'error': 'class field cannot be empty'}), 400
    
    db = get_db()
    if 'name' in data.keys():
        db.execute('UPDATE students SET name = ? WHERE id = ?', [data['name'], id])
    if 'class' in data.keys():
        db.execute('UPDATE students SET class = ? WHERE id = ?', [data['class'], id])
    db.commit()

    return jsonify({'message': f'Student {id} updated successfully'})


@app.route('/delete-student/<int:id>', methods=['DELETE'])
def delete_student(id):
    db = get_db()
    db.execute('DELETE FROM students WHERE id = ?', [id])
    db.commit()

    return jsonify({'message': f'Student {id} deleted successfully'})


@app.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    db = get_db()
    student = db.execute('SELECT * FROM students WHERE id = ?', [id]).fetchone()
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'student': student})


if __name__ == '__main__':
    app.run(debug=True)
