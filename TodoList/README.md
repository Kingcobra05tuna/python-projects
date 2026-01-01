# Todo List (CLI)

A clean and production-safe **command-line Todo List application** written in Python.  
Tasks are stored persistently using a JSON file and managed through simple keyboard commands.

## Features

- Add new tasks
- Remove tasks by number
- View tasks in a clean, numbered format
- Persistent storage using `tasks.json`
- Input validation for empty and invalid entries

## Controls

| Key | Action |
|----|-------|
| **A** | Add a task |
| **R** | Remove a task |
| **V** | View all tasks |
| **C** | Show controls |
| **Q** | Quit the application |

## How It Works

1. Program loads tasks from `tasks.json` on startup  
2. User enters a command using a single letter  
3. The corresponding action is executed safely  
4. Any change to tasks is immediately saved  
5. Program runs until the user quits

## Possible Improvements

- Mark tasks as completed
- Edit existing tasks
- Add timestamps or priorities
- Convert to OOP (`TodoList` class)
- GUI version (Tkinter / CustomTkinter)
- Package as a pip-installable CLI tool
