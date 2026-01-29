TASKS_FILE = "tasks.txt"


# ---------- File Handling ----------
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # First run, file doesn't exist yet
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# ---------- Task Features ----------
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task == "":
        print("Task cannot be empty.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks(tasks)
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)  # adjust for index
            save_tasks(tasks)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# ---------- Main Program ----------
def main():
    tasks = load_tasks()

    while True:
        print("\n==== SMART TO-DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
