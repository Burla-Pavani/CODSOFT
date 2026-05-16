tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        show_tasks()

    elif choice == '3':
        show_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        except:
            print("Invalid task number!")

    elif choice == '4':
        print("Exiting application...")
        break

    else:
        print("Invalid choice! Please try again.")