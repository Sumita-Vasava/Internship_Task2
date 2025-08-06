#Elevate Lab Internship
#Task2 : Creating a To-Do List Application (Console-based)
#Date: 5 Aug 2025
#Objective : Implementing a simple to-do list manager

#================================================================================
import os

# First we will store tasks in File
TASK_FILE = "tasks.txt"

# Load tasks from file into a list
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task to the list and save it
def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f" Tasks '{task}' added successfully!\n")

# Remove a task by number and save the updated list
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' removed successfully!\n")
        else:
            print(" Invalid task number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Main program loop, shows menu and handles user input
def main():
    print("=== To-Do List Application ===\n")
    tasks = load_tasks()

    while True:
        print("Choose an option:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting to do list, have a Goodday !!")
            break
        else:
            print(" Invalid choice. Please try again.\n" )


if __name__ == "__main__":
    main()
