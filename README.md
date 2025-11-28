Personal To-Do List Application (CLI)

This is a simple, command-line interface (CLI) application for managing personal tasks. It allows users to add, view, mark as completed, and delete tasks. All task data is persisted locally in a JSON file between sessions, eliminating the need for a complex database setup.

🚀 Getting Started

Prerequisites

You need Python 3 installed on your machine.

Installation and Setup

Clone or download the project files.

Navigate to the project directory in your terminal.

The project structure should look like this:

/todo_app 
├── todo.py         # Main application logic
├── tasks.json      # File to store tasks (created automatically if not exists)
└── README.md       # This file


Running the Application

Execute the main Python script from your terminal:

python todo.py


✨ Features

The application provides a simple menu-driven interface with the following options:

Option

Command

Description

1

Add New Task

Prompts for a title, description, and a category (Work, Personal, Urgent, etc.) before adding the task to the list.

2

View All Tasks

Displays the current list, clearly separating PENDING tasks (with indices for selection) and COMPLETED tasks.

3

Mark Task Completed

Select a pending task by its index number to mark its status as [DONE].

4

Delete Task

Select any task (pending or completed) by its index number to permanently remove it from the list.

5

Exit and Save

Closes the application and automatically saves the current state of all tasks to the tasks.json file.

📁 File Persistence

Tasks are saved using JSON (JavaScript Object Notation) format in the tasks.json file.

When the application starts, it attempts to load_tasks() from tasks.json.

Before the application exits (Option 5), it calls save_tasks() to write the current list to the file, ensuring persistence across sessions.

Developer Notes

Task Class: A Task class is used to encapsulate task properties (title, description, category, completed).

Serialization: The save_tasks function converts Task objects into simple Python dictionaries (task.__dict__) before saving them to JSON.

Deserialization: The load_tasks function reads the dictionaries from the JSON file and uses dictionary unpacking (Task(**data)) to efficiently reconstruct the Task objects.