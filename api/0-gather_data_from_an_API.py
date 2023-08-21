#!/usr/bin/python3
"""Script that prints specific information from an API"""
import json
import requests
import sys

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    request = requests.get(f'{API_URL}/users/{employee_id}/todos', params={"_expand": "user"})

    if request.status_code != 200:
        print(f"Failed to fetch data for employee ID {employee_id}")
        sys.exit(1)

    response = request.json()

    if not response:
        print(f"No data found for employee ID {employee_id}")
        sys.exit(1)

    completed_tasks = [task for task in response if task['completed']]
    if response:
        EMPLOYEE_NAME = response[0]['user']['name']
        NUMBER_OF_DONE_TASKS = len(completed_tasks)
        TOTAL_NUMBER_OF_TASKS = len(response)

        print("Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
        ))

        for task in completed_tasks:
            print("\t {}".format(task['title']))
