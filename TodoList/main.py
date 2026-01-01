import json
import os

FILE_NAME = "tasks.json"
tasks: list[str] = []

def load_tasks() -> None:
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []

def save_tasks() -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def show_controls() -> None:
    print("A -> Add a task")
    print("R -> Remove a task")
    print("V -> View tasks")
    print("C -> View controls")
    print("Q -> Quit\n")

# Actions
def add_task() -> None:
    task = input("Task name: ").strip()

    if not task:
        print("Task name cannot be empty!\n")
        return

    task = task.capitalize()

    if task in tasks:
        print("Task already exists!\n")
        return

    tasks.append(task)
    save_tasks()
    print(f"Added: {task}\n")


def remove_task() -> None:
    if not tasks:
        print("Task list is empty.\n")
        return

    view_tasks()
    try:
        index = int(input("Task number to remove: "))
        removed = tasks.pop(index - 1)
        save_tasks()
        print(f"Removed: {removed}\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")

def view_tasks() -> None:
    if not tasks:
        print("No tasks found.\n")
        return

    print(f"Tasks ({len(tasks)}):")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


# Command Map
COMMANDS = {
    "A": add_task,
    "R": remove_task,
    "V": view_tasks,
    "C": show_controls
}

def main() -> None:
    print("********** Todo List **********\n")
    load_tasks()
    show_controls()

    while True:
        cmd = input("Choice: ").strip().upper()

        if not cmd:
            print("Please enter a command.\n")
            continue

        if cmd == "Q":
            break

        action = COMMANDS.get(cmd)
        if action:
            action()
        else:
            print("Unknown command.\n")


if __name__ == "__main__":
    main()
