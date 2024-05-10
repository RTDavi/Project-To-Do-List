'''
The objective of this project is make a to do list, only with python.
I will upgrade this project when my development knowledge improves.
'''

import sys

archive_name = "to_do_list.txt"

def append_task(task):

    try:
        with open(archive_name, "a") as archive:
            return archive.write(f"{task}\n")
        
    except FileNotFoundError: # If the archive doesnt exists or is not in the same folder as the application
       with open(archive_name, "w") as archive_create:
           return archive_create.write(f"{task}\n")

        

def remove_task(taskname):

    with open(archive_name, "r") as archive:
        task_lines = archive.readlines()
    
    with open(archive_name, "w") as archive:
        for task in task_lines:
            if task.strip() != taskname: #see if is the correct line to remove
                archive.write(task)

def show_tasks(archive_name):
    try:

        with open(archive_name, "r") as archive:
            archive_read = archive.readlines()

            if archive_read:
                print("[TASK LIST]")
                for lines_enumerate, lines in enumerate(archive_read, start = 1): # Enumerate the tasks only in the print, starting from 1
                    print(f"{lines_enumerate}. {lines.strip()}") # Print the enumerated tasks.
            else:
                print("[THE LIST IS EMPTY]")

    except FileNotFoundError:
        return "[THE ARCHIVE DOENST EXIST, TRY APPENDING SOMETHING IN TO CREATE ONE.]"



print("WELCOME TO A DIGITAL TASK LIST")
while True:
    print("--------------------------------------") # A Little try to make a "Interface" for a better experience to the user
    print("WHAT DO YOU WANT TO DO?")
    print("TYPE [1] TO ADD A TASK IN THE LIST")
    print("TYPE [2] TO SEE THE TASKS")
    print("TYPE [3] TO REMOVE A TASK FROM THE LIST")
    print("TYPE [4] TO EXIT THE PROGRAM")
    print("--------------------------------------")

    answer = input("TYPE YOUR ANSWER: ")

    if answer.isdigit() != True :
        print('TYPE A REAL NUMBER')
        continue

    elif int(answer) == 1:
            task_to_append = input("INPUT WHAT YOU WILL ENTER IN THE LIST: ")
            append_task(task_to_append)
            print("THE TASK HAS BEEN APPLIED IN THE LIST ")
    
    elif int(answer) == 2:
        show_tasks(archive_name)

    elif int(answer) == 3:
        task_to_remove = input("WHAT TASK DO YOU WANT TO REMOVE?\n WRITE THE TASK HERE: ")
        remove_task(task_to_remove)
            
    elif int(answer) == 4:
        print("GOODBYE!! \n [APPLICATION ENDS]")
        sys.exit()