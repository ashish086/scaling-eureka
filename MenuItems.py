import sys 
import os
import json

# This page is responsible for the menu items

def welcome_menu():
    print("----Welcome to your daily task tracker-------\n")
    print("What would you like to do\n")
    print("The options are:\n")
    print("1.Create a new task\n")
    print("2. Update an existing task\n")
    print("3. Delete a task\n")
    print("4. To mark the task as inprogress or done\n")
    print("5. List all the tasks")
    print("6. List all the inprogress task\n")
    print("7. List all the tasks which are completed/done\n")


def capture_option_from_menu():
    print("\nPlease select an option\n")
    option = int(input())
    if (type(option)==int):
        pass
    else:
        print("Please select a valid option once again\n")
        capture_option_from_menu()

