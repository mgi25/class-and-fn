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
                (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, description TEXT, start_date DATE, end_date DATE)')
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
    

if __name__ == '__main__':
    app.run(debug=True)