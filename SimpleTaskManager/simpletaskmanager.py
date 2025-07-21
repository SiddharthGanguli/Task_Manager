import time

tasks = []

def add_task(task_name):
    task = {
        'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'task': task_name
    }
    tasks.append(task)

user_input = input("Do you have any active tasks? (yes/no): ")

if user_input.lower() in ['yes', 'y']:
    numberOfInputs = int(input("How many tasks do you want to add? "))
    for i in range(numberOfInputs):
        task_name = input(f"Enter task #{i+1} name: ")
        add_task(task_name)
else:
    print("No tasks added. Thank you!")

print("\nYour Tasks:")
for t in tasks:
    print(f"Time: {t['time']}  |  Task: {t['task']}")
