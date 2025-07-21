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
    while True:
        try:
            numberOfInputs = int(input("How many tasks do you want to add? "))
            if numberOfInputs <= 0:
                print("Please enter a number greater than 0.")
                continue
            break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for i in range(numberOfInputs):
        task_name = input(f"Enter task ->{i+1} name: ")
        add_task(task_name)
else:
    print("No tasks added. Thank you!")

print("\nYour Tasks:")
for t in tasks:
    print(f"Time: {t['time']}  |  Task: {t['task']}")


def adding_features(tasks):
    noOftask=int(input("How many task you want to add ? "))
    for i in range (noOftask):
        task_name = input(f"Enter task ->{i+1} name: ")
        add_task(task_name)
        print(f"Congratulation your {noOftask+1} added")


print("Operations are also available to performe")
user_input2 = input("Would you like to perform any actions (Add, Edit, Delete, View)? Enter yes or no: ")

if user_input2.lower() in ['yes','y']:
    print("Available actions are Add, Edit, Delete, View")
    user_input3 = input("Enter the action you want to perform: ")
    if user_input3.lower() in ['add', 'a']:
        adding_features(tasks)