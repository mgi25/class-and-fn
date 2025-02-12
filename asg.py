#create a FLASK API, which Data base connecitivity that will store your tasks, [title, description, start_date, end_date,status]

#1. adding new tasks
#2. viewing all tasks
#3. view specific tasks
#4. changing the status of task
#5. update the description of a task


from flask import Flask,request,g,jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'task'

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
                (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, description TEXT, start_date )')
    db.commit()




if __name__ == '__main__':
    app.run(debug=True)