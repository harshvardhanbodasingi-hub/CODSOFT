import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_menu():
    print("\n" + "=" * 40)
    print("        TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as completed")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit")
    print("=" * 40)


def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks found. Add a task first!")
        return

    print("\nYour Tasks:")
    print("-" * 70)
    for idx, task in enumerate(tasks, start=1):
        status = "✔ DONE" if task.get("completed") else "✖ PENDING"
        print(f"ID: {idx}")
        print(f"  Title      : {task.get('title')}")
        print(f"  Description: {task.get('description')}")
        print(f"  Due Date   : {task.get('due_date')}")
        print(f"  Priority   : {task.get('priority')}")
        print(f"  Status     : {status}")
        print("-" * 70)


def add_task(tasks):
    print("\nAdd New Task")
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty. Task not added.")
        return

    description = input("Enter description (optional): ").strip()
    due_date = input("Enter due date (e.g. 2025-12-01) (optional): ").strip()
    priority = input("Enter priority (Low/Medium/High) (optional): ").strip()

    task = {
        "title": title,
        "description": description if description else "-",
        "due_date": due_date if due_date else "-",
        "priority": priority if priority else "Medium",
        "completed": False,
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def get_task_index(tasks, prompt="Enter task ID: "):
    if not tasks:
        print("No tasks available.")
        return None
    try:
        task_id = int(input(prompt))
        if 1 <= task_id <= len(tasks):
            return task_id - 1
        else:
            print("Invalid ID. Please try again.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def mark_task_completed(tasks):
    print("\nMark Task as Completed")
    list_tasks(tasks)
    idx = get_task_index(tasks)
    if idx is None:
        return
    if tasks[idx]["completed"]:
        print("Task is already marked as completed.")
    else:
        tasks[idx]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")


def edit_task(tasks):
    print("\nEdit Task")
    list_tasks(tasks)
    idx = get_task_index(tasks)
    if idx is None:
        return

    task = tasks[idx]
    print("\nLeave input empty to keep current value.")
    new_title = input(f"New title (current: {task['title']}): ").strip()
    new_desc = input(f"New description (current: {task['description']}): ").strip()
    new_due = input(f"New due date (current: {task['due_date']}): ").strip()
    new_priority = input(f"New priority (current: {task['priority']}): ").strip()

    if new_title:
        task["title"] = new_title
    if new_desc:
        task["description"] = new_desc
    if new_due:
        task["due_date"] = new_due
    if new_priority:
        task["priority"] = new_priority

    save_tasks(tasks)
    print("Task updated successfully!")


def delete_task(tasks):
    print("\nDelete Task")
    list_tasks(tasks)
    idx = get_task_index(tasks)
    if idx is None:
        return

    deleted_task = tasks.pop(idx)
    save_tasks(tasks)
    print(f"Deleted task: {deleted_task['title']}")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
