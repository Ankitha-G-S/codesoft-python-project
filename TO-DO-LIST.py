tasks = []

def add_task(title, description, due_date):
    tasks.append({"title": title, "description": description, "due_date": due_date, "completed": False})

def view_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

def mark_task_complete(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]['completed'] = True
    else:
        print("Invalid task index")

def delete_task(index):
    if 0 < index <= len(tasks):
        del tasks[index - 1]
    else:
        print("Invalid task index")

# Example usage
add_task("Complete assignment", "Finish the assignment", "2024-04-10")
add_task("Buy groceries", "Milk, eggs, bread", "2024-04-07")
view_tasks()
mark_task_complete(1)
delete_task(2)
view_tasks()
