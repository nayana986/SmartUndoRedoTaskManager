Smart Undo-Redo Task Manager

📌 Project Description

The Smart Undo-Redo Task Manager is a terminal-based application developed using Python.
It allows users to manage tasks by adding, deleting, displaying tasks, and undoing the last action.

This project demonstrates the implementation of important Data Structures concepts such as:

- Singly Linked List
- Stack (Array-based)
- Time Complexity Analysis

The main objective of this project is to show how Stacks can be used to implement Undo operations similar to real-world applications.

---

🎯 Features

- Add new tasks
- Delete existing tasks
- Display all tasks
- Undo the last operation
- Menu-based user interface

---

🛠️ Technologies Used

- Python
- Data Structures
  - Singly Linked List
  - Stack

---

📂 Project Structure

SmartUndoRedoTaskManager
│
├── task_manager.py
└── README.md

---

⚙️ How to Run the Project

Step 1: Install Python

Download Python from
https://www.python.org

Verify installation:

python --version

---

Step 2: Clone the Repository

git clone https://github.com/yourusername/SmartUndoRedoTaskManager.git

---

Step 3: Navigate to the Project Folder

cd SmartUndoRedoTaskManager

---

Step 4: Run the Program

python task_manager.py

---

🧠 Data Structures Used

1. Singly Linked List

Used to store the current list of tasks.

Example:

Task1 → Task2 → Task3 → NULL

---

2. Stack

Used to store history of operations for implementing the Undo feature.

Example stack:

Add Task1
Add Task2
Delete Task2

Undo operation pops the last action.

---

⏱ Time Complexity

Operation| Time Complexity
Add Task| O(n)
Delete Task| O(n)
Display Tasks| O(n)
Undo Operation| O(1)

---

📌 Example Output

1 Add Task
2 Delete Task
3 Display Tasks
4 Undo
5 Exit

Enter choice: 1
Enter task name: Study Python

Enter choice: 3
1 - Study Python

---

🚀 Future Improvements

- Add Redo functionality
- Add Graphical User Interface (GUI)
- Store tasks using a database
- Convert into a web application

---

👩‍💻 Author

Nayana Dedhipya Damera
Computer Science Engineering (AI & ML)

---

📄 License

This project is developed for educational and learning purposes.
