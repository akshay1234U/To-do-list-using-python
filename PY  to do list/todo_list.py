import json

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
