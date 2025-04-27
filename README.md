
# 📝 Flask To-Do List API

A simple RESTful API built with *Flask* and *SQLite* that allows you to create, read, update, and delete tasks.

---

📚 What We Did

- Built a basic *Flask* server.
- Created a *SQLite* database to store tasks.
- Implemented full *CRUD* operations:
  - Create Task (POST)
  - Get All Tasks (GET)
  - Update Task (PUT)
  - Delete Task (DELETE)
- Built and tested the API using *Postman* (or Thunder Client).

---

🛠 Technologies Used

- Python 3
- Flask
- SQLite3
- Postman (for API testing)

---

🚀 How to Run the Project

1. *Clone the repository:*
   bash
   git clone https://github.com/BelalMedhat76/Flask-To-Do-List-API.git
   cd Flask-To-Do-List-API
   

2. *Install dependencies:*
   bash
   pip install flask
   

3. *Run the app:*
   bash
   python3 app.py
   ```

4. Access the API:
   - View all tasks ➔ [http://127.0.0.1:5000/api/tasks](http://127.0.0.1:5000/api/tasks)

---

🎯 API Endpoints

| Method | Endpoint | Description |
|:------:|:---------|:------------|
| GET | /api/tasks | Get all tasks |
