# todo_list.py

tasks = []

def create_task():
    task_description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high, medium, low): ")
    task = {"description": task_description, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(task)
    print("Task created successfully!")

def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {status}")

def update_task():
    task_id = int(input("Enter task ID to update: ")) - 1
    if task_id < len(tasks):
        task_description = input("Enter new task description: ")
        due_date = input("Enter new due date (YYYY-MM-DD): ")
        priority = input("Enter new priority (high, medium, low): ")
        tasks[task_id]["description"] = task_description
        tasks[task_id]["due_date"] = due_date
        tasks[task_id]["priority"] = priority
        print("Task updated successfully!")
    else:
        print("Invalid task ID!")

def complete_task():
    task_id = int(input("Enter task ID to complete: ")) - 1
    if task_id < len(tasks):
        tasks[task_id]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task ID!")

def delete_task():
    task_id = int(input("Enter task ID to delete: ")) - 1
    if task_id < len(tasks):
        del tasks[task_id]
        print("Task deleted successfully!")
    else:
        print("Invalid task ID!")

def search_tasks():
    search_query = input("Enter search query: ")
    results = [task for task in tasks if search_query in task["description"]]
    if results:
        print("Search results:")
        for i, task in enumerate(results, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {status}")
    else:
        print("No tasks found!")

def main():
    while True:
        print("To-Do List App")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Search Tasks")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            search_tasks()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
    # todo_list_gui.py

import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        self.task_list_box = tk.Listbox(self.task_list_frame, width=40)
        self.task_list_box.pack(fill="both", expand=True)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x")

        self.create_button = tk.Button(self.button_frame, text="Create Task", command=self.create_task)
        self.create_button.pack(side="left")

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side="left")

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side="left")

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="left")

        self.search_button = tk.Button(self.button_frame, text="Search Tasks", command=self.search_tasks)
        self.search_button.pack(side="left")

    def create_task(self):
        task_description = tk.simpledialog.askstring("Create Task", "Enter task description")