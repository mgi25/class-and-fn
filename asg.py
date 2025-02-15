#create a FLASK API, which Data base connecitivity that will store your tasks, [title, description, start_date, end_date,status]

#1. adding new tasks
#2. viewing all tasks
#3. view specific tasks
#4. changing the status of task
#5. update the description of a task


from flask import Flask,request,g,jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'task.db'

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
    db.execute('CREATE TABLE IF NOT EXISTS task\
                (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, description TEXT, start_date DATE, end_date DATE,status DEFAULT "pending")')
    db.commit()

@app.route('/add-task',methods = ['POST'])
def add_task():
    data = request.json
    if 'title' and 'description' and 'start_date' and 'end_date' not in data.keys():
        return jsonify({'error':'title, description,start_date,end_date fileds cannot be empty'})
    db = get_db()
    db.execute('INSERT INTO task (title,description,start_date,end_date) values (?,?,?,?)',
               [data['title'],data['description'],data['start_date'],data['end_date']])
    db.commit()
    return jsonify({'msg':f'task {data['title']} added sucessfully'})


#view

@app.route('/view',methods = ['GET'])
def view():
    db = get_db()
    task = db.execute('SELECT * from task').fetchall()
    return jsonify({'task':task})



# specific task 

@app.route('/search/<int:id>',methods = ['GET'])
def search(id):
    db = get_db()
    task = db.execute('SELECT * FROM task where id = ?',[id]).fetchone()
    if task is None:
        return jsonify({'msg':'no id found'})
    return jsonify({'task':task})
    
# status update


@app.route('/status/<int:id>',methods =['PUT'])
def status(id):
    data = request.json
    if not 'status' in data.keys():
        return jsonify({'error':'cannot be empty'}),400
    if 'status'in data.keys() and data['status'].strip() =='':
        return jsonify({'error':'cannot be empty'}), 400
    db = get_db()
    if 'status' in data.keys():
        db.execute('UPDATE task SET status = ? WHERE id = ?', [data['status'],id])
        db.commit()
        return jsonify({'msg':'status updated sucessfully'})


#update description
@app.route('/description/<int:id>',methods =['PUT'])
def description(id):
    data = request.json
    if not 'description' in data.keys():
        return jsonify({'error':'cannot be empty'}),400
    if 'description'in data.keys() and data['description'].strip() =='':
        return jsonify({'error':'cannot be empty'}), 400
    db = get_db()
    if 'description' in data.keys():
        db.execute('UPDATE task SET description = ? WHERE id = ?', [data['description'],id])
        db.commit()
        return jsonify({'msg':'description updated sucessfully'})


if __name__ == '__main__':
    app.run(debug=True)