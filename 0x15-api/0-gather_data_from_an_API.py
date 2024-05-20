#!/usr/bin/python3
'''
Python script that, using the jsonplaceholder.typicode.com/,
for a given employee ID, returns information about
his/her TODO list progress
'''
import requests
import sys


def get_todo_list(employee_id):
    '''Function to get the TODO list'''
    # Construct the URLs for fetching user information and TODO list
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Send HTTP requests to fetch user information and TODO list
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    # Check if both requests are successful
    if user_response.status_code == 200 and todo_response.status_code == 200:
        # Extract user name from the response
        user_name = user_response.json().get('name')

        # Extract TODO list from the response
        todo_list = todo_response.json()

        # Count completed tasks
        completed_tasks = [task for task in todo_list if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_list)

        # Print the TODO list progress
        print(f'Employee Name: {user_name}')
        print(f'To Do Count: {total_tasks}')
        print(f'Task completion: ({num_completed_tasks}/{total_tasks})')

        for task in completed_tasks:
            print(f"\t{task['title']}")  # Adjusted task formatting
    else:
        print('Error: Could not retrieve data')


if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Usage: ./0-gather_data_from_an_API.py <employee id>')
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Call the function to fetch and display the TODO list progress
    get_todo_list(employee_id)
