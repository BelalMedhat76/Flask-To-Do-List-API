
from flask import Flask, render_template, request, redirect, url_for,jsonify
import sqlite3

app = Flask(__name__)

def init_sqlite_db():
    conn = sqlite3.connect('tasks.db')
    print("Database opened successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()




@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    tasks_list = []
    for task in tasks:
        tasks_list.append({
            'id': task[0],
            'task': task[1]
        })

    return jsonify(tasks_list)





@app.route('/api/tasks', methods=['POST'])
def add_task():
    new_task = request.json.get('task')

    if not new_task:
        return jsonify({'error': 'Task is required!'}), 400

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (new_task,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task added successfully!'}), 201





@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json.get('task')

    if not updated_task:
        return jsonify({'error': 'Task is required!'}), 400

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task=? WHERE id=?", (updated_task, task_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated successfully!'})

    
    
    

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Task deleted successfully!'})



#_______-to make html template work remove all comments and remove the upove code for APIS____________

# @app.route('/')
# def index():
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM tasks")
#     tasks = cursor.fetchall()
#     conn.close()
#     return render_template('index.html', tasks=tasks)


# @app.route('/add', methods=['POST'])
# def add_task():
#     if request.method == 'POST':
#         task = request.form['task']
#         conn = sqlite3.connect('tasks.db')
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))




# @app.route('/delete/<int:task_id>', methods=['POST'])
# def delete_task(task_id):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index')) 
  
  
  


# @app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
# def edit_task(task_id):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()

#     if request.method == 'POST':
#         new_task = request.form['task']
#         cursor.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))

#     else:
#         cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
#         task = cursor.fetchone()
#         conn.close()
#         return '''
#             <h1>Edit Task</h1>
#              <form method="POST">
#                 <input type="text" name="task" value="{0}" required>
#                 <button type="submit">Update</button>
#             </form>
#         '''.format(task[1])
  

if __name__== "__main__":
    app.run(debug=True)