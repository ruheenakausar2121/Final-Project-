# Personal To-Do List Application

A simple **Personal To-Do List Application** built with **Python**, designed as a mini-project for **VaultofCode Internship**.  
This project demonstrates **Object-Oriented Programming (OOP)**, **file handling**, and building a **user-friendly CLI**.

---

## Features

- **Task Management**
  - Add tasks with a title, description, and category.
  - Mark tasks as completed.
  - Delete tasks.

- **Categorization**
  - Organize tasks into categories: Work, Personal, Urgent, Shopping, or Other.

- **Persistence**
  - Tasks are saved to a local `tasks.json` file, retaining progress between sessions.

- **User-Friendly CLI**
  - Simple command-line interface with clear menus and prompts.

---

## Key Concepts Used

- **Object-Oriented Programming (OOP)**
  - Task class with attributes and methods.
- **File Handling**
  - Saving and loading tasks using JSON serialization.
- **Dictionary Unpacking**
  - Loading JSON data directly into Task objects.

---

## Installation

1. Ensure **Python 3.x** is installed on your system.
2. Clone this repository or download the project files.
3. (Optional) Create a virtual environment:

```bash
python -m venv .venv
Activate the virtual environment:

PowerShell:

powershell
Copy code
.\.venv\Scripts\Activate.ps1
CMD:

c
Copy code
.\.venv\Scripts\activate.bat
How to Run
In the project directory, run:

bash
Copy code
python todo.py
Follow the on-screen menu to add, view, complete, or delete tasks.

File Structure
bash
Copy code
/todo_app
├── todo.py         # Main application logic
├── tasks.json      # Stores tasks between sessions
└── README.md       # Project documentation
Sample Usage
pgsql
Copy code
1. Add New Task
2. View All Tasks
3. Mark Task Completed
4. Delete Task
5. Exit and Save
Example workflow:

Add a task “Finish Assignment” under “Work” category.

View the task in the list.

Mark it completed.

Exit and save tasks in tasks.json.

Author
Shaik Ruheena Kausar
Built as a Python mini-project for VaultofCode Internship, focusing on CLI, OOP, and file handling.
