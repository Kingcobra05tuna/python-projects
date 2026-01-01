tasks = [] # 'Task1', 'Task2'

def showControls() -> None:
    print("A -> Add a task to the list.")
    print("R -> Remove a valid task from the list.")
    print("V -> View the list.")
    print("C -> View the controls.")
    print("Q -> Quit.\n")

def add(task: str) -> None:
    if task not in tasks:
        tasks.append(task)
        print(f"Added: {task} to the list!\n")
    else:
        print("Task is already in the list!\n")

def remove(task: str) -> None:
    if task in tasks:
        tasks.remove(task)
        print(f"Removed: {task} from the list!")
    else:
        print("Specified task was not found.")

def view() -> None:
    print(f"Viewing current tasks ({len(tasks)}) \n")
    print(str(tasks))

def getInput(message: str, whole: bool) -> str:
    inp = input(message)

    if whole: return inp
    else: return inp[0]

commandMap = {
    "A": "add(getInput('Name?: ', True).capitalize())",
    "R": "remove(getInput('Name?: ', True).capitalize())",
    "V": "view()",
    "C": "tutorial()",
    "Q": "quit()"
}

def main() -> None:
    print("********** Todo list **********\n")
    showControls()

    while True:
        inp = getInput("Please enter your choice: ", False).strip().upper()
        print()
        if commandMap[inp]:
            eval(commandMap[inp])
        else:
            print("Command not found, please try again.")
        
if __name__ == "__main__":
    main()
