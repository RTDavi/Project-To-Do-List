'''
The objective of this project is make a to do list, only with python.
I will upgrade this project when my development knowledge improves
'''

import sys

print("WELCOME TO THE DIGITAL TO-DO-LIST")
while True:
    print("--------------------------------------")
    print("WHAT DO YOU WANT TO DO IN THE LIST?")
    print("1. ")
    print("TYPE [2] TO SEE THE LIST")
    print("TYPE [3] TO REMOVE SOMETHING IN THE LIST")
    print("TYPE [4] TO EDIT SOMETHING IN THE LIST")
    print("TYPE [5] TO EXIT THE PROGRAM")
    print("--------------------------------------")

    answer = input("TYPE YOUR ANSWER:")

    if answer.isdigit() != True :
        print('TYPE A REAL NUMBER')
        continue

    if int(answer) == 1:
        with open("to_do_list.txt", "w") as archive:
            writing_the_list = input("What you will put in the list?")
            archive.write(f'1. {writing_the_list}')
    
    if int(answer) == 5:
        sys.exit()
        