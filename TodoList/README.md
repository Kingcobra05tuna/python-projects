# Todo List (CLI)

A clean and production-safe **command-line Todo List application** written in Python.  
Tasks are stored persistently using a JSON file and managed through simple keyboard commands.

## Features

- Add new tasks
- Remove tasks by number
- View tasks in a clean, numbered format
- Persistent storage using `tasks.json`
- Input validation for empty and invalid entries
- Safe command handling (no `eval`)
- Minimal and beginner-friendly codebase

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


## Code Overview

- **Persistent Storage**
  - Tasks are saved and loaded using a JSON file
  - Data is preserved between program runs

- **Command System**
  - Uses a dictionary mapping commands to functions
  - Eliminates the use of `eval()` for safety

- **Input Validation**
  - Prevents empty task names
  - Handles invalid command input
  - Catches incorrect task numbers

- **Task Formatting**
  - Tasks are displayed as a numbered list
  - Improves readability and UX

## Requirements

- Python 3.10+
- No external libraries required

## Known Limitations

- Single-user only
- No task completion status
- No task editing feature

## Possible Improvements

- Mark tasks as completed
- Edit existing tasks
- Add timestamps or priorities
- Convert to OOP (`TodoList` class)
- GUI version (Tkinter / CustomTkinter)
- Package as a pip-installable CLI tool
