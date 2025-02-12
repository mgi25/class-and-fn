#create a FLASK API, which Data base connecitivity that will store your tasks, [title, description, start_date, end_date,status]

#1. adding new tasks
#2. viewing all tasks
#3. view specific tasks
#4. changing the status of task
#5. update the description of a task


from flask import Flask,request,g,jsonify
import sqlite3

app = Flask(__name__)




if __name__ == '__main__':
    app.run(debug=True)