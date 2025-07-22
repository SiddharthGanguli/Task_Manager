import time

tasks = []
import time

tasks = []


def add_task(task_name, serial_no):
    task = {
        'serial_no': serial_no,
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
        task_name = input(f"Enter task #{i+1} name: ")
        serial_no = i + 1
        add_task(task_name, serial_no)
else:
    print("No tasks added. Thank you!")

if tasks:
    print("\nYour Tasks:")
    for t in tasks:
        print(f"#{t['serial_no']} | Time: {t['time']} | Task: {t['task']}")



def adding_features(tasks):
    noOftask=int(input("How many task you want to add ? "))
    for i in range (noOftask):
        task_name = input(f"Enter task ->{i+1} name: ")
        add_task(task_name)
        print(f"Congratulation your {noOftask+1} added")

def removing_features(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    print("\nYour Tasks:")
    for t in tasks:
        print(f"#{t['serial_no']} | Time: {t['time']} | Task: {t['task']}")

    while True:
        try:
            serial_no_input = int(input("Enter the Serial Number of the task you want to remove: "))
            found = False
            for i, task in enumerate(tasks):
                if task['serial_no'] == serial_no_input:
                    tasks.pop(i)
                    print(f"Task #{serial_no_input} removed successfully.")
                    found = True
                    break
            if not found:
                print("Invalid Serial Number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
print("\nYour Tasks:")

            
def editing_features(tasks):
    if not tasks:
        print("No tasks available to edit.")
        return

    try:
        user_input = int(input("Enter the Serial Number of the task you want to edit: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for task in tasks:
        if task['serial_no'] == user_input:
            new_task_name = input("Enter the updated task name: ")
            task['task'] = new_task_name
            print(f"Task #{user_input} updated successfully.")
            return

    print(f"No task found with Serial Number #{user_input}.")


print("Operations are also available to performs")
user_input2 = input("Would you like to perform any actions (Add, Edit, Delete, View)? Enter yes or no: ")

if user_input2.lower() in ['yes','y']:
    print("Available actions are Add, Edit, Delete, View")
    user_input3 = input("Enter the action you want to perform: ")
    if user_input3.lower() in ['add', 'a']:
        adding_features(tasks)
    elif user_input3.lower() in ['remove','delete','r','d']:
        removing_features(tasks)

    elif user_input3.lower() in ['edit','e']:
        editing_features(tasks)
print("Final tasks : ")
for t in tasks:
    print(f"#{t['serial_no']} | Time: {t['time']} | Task: {t['task']}")