# Todo List (CLI)

A simple command-line based **Todo List application** written in Python.  
Add, remove, and view tasks using keyboard commands.

## Features

- Add new tasks to the list
- Remove existing tasks
- View all current tasks
- Duplicate task prevention
- Case-insensitive command system
- Simple and minimal CLI interface

## Controls

| Key | Action |
|----|-------|
| **A** | Add a task |
| **R** | Remove a task |
| **V** | View all tasks |
| **C** | Show controls |
| **Q** | Quit the program |

## How It Works

1. Program starts and displays available controls  
2. User enters a single-letter command  
3. Based on the command:
   - Task is added
   - Task is removed
   - Task list is displayed
4. Program runs in a loop until **Q** is pressed


## Code Structure

- `tasks`  
  Stores all tasks as a list of strings.

- `add(task)`  
  Adds a task if it does not already exist.

- `remove(task)`  
  Removes a task if it exists in the list.

- `view()`  
  Displays all tasks and task count.

- `getInput(message, whole)`  
  Handles user input:
  - Full string input
  - Single-character command input

- `commandMap`  
  Maps commands to executable actions.

- `main()`  
  Entry point that runs the main loop.

## Requirements

- Python 3.x  
- No external libraries required

## Known Issues / Limitations

- Uses `eval()` for command execution (not recommended for production)
- No persistent storage (tasks reset on restart)
- No input validation for empty commands
- Tasks are stored as a raw list (no formatting)

## Possible Improvements

- Replace `eval()` with function references
- Add file saving/loading (JSON or TXT)
- Numbered task display
- Task editing feature
- GUI version (Tkinter / CustomTkinter)
- Error handling for invalid commands

---

**Minimal, fast, and educational.**
Perfect for learning CLI logic and command handling.
