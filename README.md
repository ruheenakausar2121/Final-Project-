# ✅ Personal To-Do List Application (CLI)

A lightweight, beginner-friendly **command-line task manager** built with Python.  
No database, no dependencies — just pure Python and a JSON file to keep your tasks organized across sessions.

---

## 📌 About the Project

This CLI application lets you manage your daily tasks right from the terminal. It supports adding, viewing, completing, and deleting tasks — all persisted locally in a `tasks.json` file so your data is never lost between sessions.

Built as a clean demonstration of:
- Object-Oriented Programming (OOP) with Python
- File I/O and JSON serialization/deserialization
- Menu-driven CLI application design

---

## ✨ Features

| Option | Feature | Description |
|--------|---------|-------------|
| `1` | ➕ Add New Task | Enter a title, description, and category (Work / Personal / Urgent / etc.) |
| `2` | 📋 View All Tasks | Displays **PENDING** and **COMPLETED** tasks separately with index numbers |
| `3` | ✔️ Mark as Completed | Select a pending task by index to mark it as `[DONE]` |
| `4` | 🗑️ Delete Task | Permanently remove any task (pending or completed) by index |
| `5` | 💾 Exit & Save | Saves all tasks to `tasks.json` and exits the application |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your machine
- No external libraries needed — uses only the Python standard library!

Check your Python version:
```bash
python --version
```

### Installation

**Step 1:** Clone or download the project
```bash
git clone https://github.com/YOUR_USERNAME/todo-cli-app.git
cd todo-cli-app
```

**Step 2:** Run the application
```bash
python todo.py
```

That's it — no `pip install` needed! 🎉

---

## 📁 Project Structure

```
todo_app/
├── todo.py        # Main application logic
├── tasks.json     # Auto-generated task storage file
└── README.md      # Project documentation
```

---

## 🖥️ How It Works

When you run the app, you'll see a simple menu:

```
=============================
     MY TO-DO LIST APP
=============================
  1. Add New Task
  2. View All Tasks
  3. Mark Task Completed
  4. Delete Task
  5. Exit and Save
=============================
Enter your choice:
```

Tasks are displayed like this:

```
--- PENDING ---
[1] Buy groceries (Personal) - Pick up milk and eggs
[2] Finish report (Work) - Submit by Friday

--- COMPLETED ---
[DONE] Morning workout (Urgent)
```

---

## 🔧 Technical Details

### Task Class
Each task is represented as an object with the following properties:

```python
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
```

### File Persistence

**Saving tasks** — converts Task objects to dictionaries before writing to JSON:
```python
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)
```

**Loading tasks** — reads JSON and reconstructs Task objects using dictionary unpacking:
```python
def load_tasks():
    with open("tasks.json", "r") as f:
        return [Task(**data) for data in json.load(f)]
```

---

## 🗂️ Sample `tasks.json`

```json
[
    {
        "title": "Buy groceries",
        "description": "Pick up milk and eggs",
        "category": "Personal",
        "completed": false
    },
    {
        "title": "Morning workout",
        "description": "30 min cardio",
        "category": "Urgent",
        "completed": true
    }
]
```

---

## 👩‍💻 Developer

**Shaik Ruheena Kausar**  
Engineering Student  
🔗 [GitHub Profile](https://github.com/ruheenakausar2121)

---

## 📄 License

This project is free to use for learning and personal projects.  
Feel free to fork and improve it! ⭐

---

> 💡 **Tip:** Add this project to your portfolio — it showcases Python OOP, file handling, and clean CLI design all in one!
