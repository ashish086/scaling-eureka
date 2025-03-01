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
    if create_taskfile:
        with open(file_name,"r") as file:
            tasks = json.load(file)
    else:
        tasks = []
    task_id = len(tasks)+1
    task_details = {
        "Task_id":task_id,
        "Task_name": task_name
   }
    tasks.append(task_details)
    with open(file_name,"w") as file:
        json.dump(tasks,file,indent=1)
    print(f"Task '{task_name}' has been created with ID: {task_id}")


def list_updation_options():
    print("Do you want to display the list of tasks or do you have a task id to update?\n")
    print("If you want to display the list of all the tasks enter number 1\n")
    print("If you want to update the task directly based on Task id enter number 2\n")
    option_capture = int(input())
    if option_capture==1:
        #Function call to display all the tasks
        pass
    elif option_capture==2:
        #Function call to update the task
        update_task()
    else:
        print("Enter a valid option")
        list_updation_options()
        

def update_task():
    #THIS function is responsible for updating the task in json on the basis of id
    print("Enter the value of the task id which needs to be updated")
    task_update_id = int(input())
    if type(task_update_id)==int:
        return 0
    else:
        update_task()
    
