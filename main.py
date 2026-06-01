# to-do list application in the terminal

from sys import exit
from prettytable import PrettyTable
from datetime import datetime

# Logo

print('''
                                                                     
▄▄▄▄▄▄▄▄▄       ▄▄         ▄▄                     ▄▄▄▄               
▀▀▀███▀▀▀       ██         ██ ▀▀         ██     ▄██▀▀██▄             
   ███ ▄███▄ ▄████ ▄███▄   ██ ██  ▄█▀▀▀ ▀██▀▀   ███  ███ ████▄ ████▄ 
   ███ ██ ██ ██ ██ ██ ██   ██ ██  ▀███▄  ██     ███▀▀███ ██ ██ ██ ██ 
   ███ ▀███▀ ▀████ ▀███▀   ██ ██▄ ▄▄▄█▀  ██     ███  ███ ████▀ ████▀ 
                                                         ██    ██    
                                                         ▀▀    ▀▀    

''')

# Checking Variables
has_removed_tasks = False
has_completed_tasks = False
has_updated_tasks = False
has_viewed_tasks = False
has_added_tasks = False
is_valid_task = False

# Other variables

actions = ["add", "remove", "view", "complete", "update"]

task_counter = 0

todo_table = PrettyTable()
todo_table.field_names = ["Index", "Tasks", "Status", "Date Added"]

tasks = []

status = []

# Functions for the actions

def add_tasks():

    global task_counter

    task = input("Enter task to add: ")
    status_input = input("Enter the status of the task: ")
    tasks.append(task)
    status.append(status_input)

# Functions for the actions
def remove_tasks():
    removed_task = input("Enter the task you want to remove: ")
    if removed_task in tasks:
        tasks.remove(removed_task)
        print("Task removes succsessfuly!")
    else:
        print("Task does not exist.")

def view_tasks():
    print(todo_table)

def complete_tasks():
    pass

def update_tasks():
    pass

def check_valid_action():
        while not has_completed_tasks:
            try:
                action = input("That action does not exist. Enter a valid action (Enter 'Q' to quit): ")
                if action.lower() == "q":
                    exit()
                elif action == "add":
                    add_tasks()
                elif action == "remove":
                    remove_tasks()
                elif action == "view":
                    view_tasks()
                elif action == "complete":
                    complete_tasks()
                elif action == "update":
                    update_tasks()

            except KeyboardInterrupt:
                print("         🔴 Oops... it looks like the program was interrupted. Restart the program to continue.")
                exit()

            except:
                while not is_valid_task:
                    action = input("That action does not exist. Enter a valid action (Enter 'Q' to quit): ")
                    if action.lower() == "q":
                        break
                        exit()
                    else:
                        is_valid_task = True
                        is_valid_task = False
                        break
# Notes
print('Enter "Q" to quit')

# Main loop

while True:
    try:

        task_duplicate = todo_table

        action = input("Enter an action (Add, Remove, View, Complete, Update): ")
        action = action.lower()

        if action == "add":
            add_tasks()
        elif action == "remove":
            remove_tasks()
        elif action == "view":
            view_tasks()
        elif action == "complete":
            complete_tasks()
        elif action == "update":
            update_tasks()
        elif action == "q":
            exit()
        else:
            check_valid_action()

    except KeyboardInterrupt:
        print("         🔴 Oops... it looks like the program was interrupted. Restart the program to continue.")
        break