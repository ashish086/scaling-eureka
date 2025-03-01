import os 
import sys
import json

''' 
This file is responsible for CRUD operations in Tasktracker
Function list:
1. Create task and save it in json file (args: task name, id for the task name)
2. Update the already created based on id (feature can be to update task by its name)
3. Delete a created task based on id (feature can be to delete task by its name)

'''
file_name = "taskslist.json"

def create_taskfile():
    try:
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.write("{}")  
            return "File created"
        else:
            return "File exists"
    except Exception as e:
        return(f"Error creating file: {e}")
    
def create_task():
    print("Please enter the task name\n")
    task_name = input()
    pass



