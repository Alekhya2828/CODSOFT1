import os

# Load the tasks from the file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]  # Return tasks without newline characters
    else:
        return []  # Return an empty list if no file exists

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display the to-do list
def display_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

# Add a new task
def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added to your to-do list.")

# Update an existing task
def update_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number you want to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number - 1] = new_task  # Update the task
            save_tasks(tasks)
            print(f"Task #{task_number} has been updated to: {new_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Mark a task as completed (delete it)
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number you want to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)  # Remove the task from the list
            save_tasks(tasks)
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Main function to interact with the user
def main():
    tasks = load_tasks()  # Load tasks from the file

    while True:
        print("\nTo-Do List Application")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)  # Display the tasks
        elif choice == '2':
            add_task(tasks)  # Add a new task
        elif choice == '3':
            update_task(tasks)  # Update an existing task
        elif choice == '4':
            delete_task(tasks)  # Delete a task
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break  # Exit the application
        else:
            print("Invalid choice. Please choose between 1 and 5.")

# Run the application
if __name__ == "__main__":
    main()
