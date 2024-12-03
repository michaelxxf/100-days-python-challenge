# Simple To-Do List Application

def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list!\n")

def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed from the list!\n")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.\n")

def main():
    tasks = []
    while True:
        print("To-Do List App")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!\n")

main()