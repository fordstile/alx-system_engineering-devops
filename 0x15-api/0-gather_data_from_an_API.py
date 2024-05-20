#!/usr/bin/python3
'''Python script that, using this jsonplaceholder.typicode.com/,
for a given employee ID, returns information about
his/her TODO list progress'''
import requests

# Base URL of the REST API
REST_API = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    # Send a GET request to fetch user information
    user_info = requests.get(f"{REST_API}/users/{employee_id}").json()
    # Send a GET request to fetch TODO list information
    todo_list = requests.get(f"{REST_API}/todos").json()

    # Extract employee name
    employee_name = user_info.get('name')

    # Filter tasks associated with the given employee ID
    tasks = [task for task in todo_list if task['userId'] == employee_id]
    # Count completed tasks
    completed_tasks = sum(1 for task in tasks if task['completed'])

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{len(tasks)}):")
    for task in tasks:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    # Simulate command-line argument (employee ID)
    employee_id = 2
    # Fetch and display TODO list progress for the employee
    get_employee_todo_progress(employee_id)
