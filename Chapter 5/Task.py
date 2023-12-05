# Define an empty list
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ") #Let user input
    tasks.append({"task": task, "completed": False}) #Default Define
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.") # Use a not gate that dear Neal told us
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1): #Find tasks? (From StackOverflow)
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

# Function to mark a task as complete
def mark_complete():
    view_tasks()
    task_num = int(input("Enter the task number to mark as complete: ")) #Let user input numbers
    if 1 <= task_num <= len(tasks): #Check whether the Number is valid
        tasks[task_num - 1]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_task() #I LOVE FUNCTION
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
