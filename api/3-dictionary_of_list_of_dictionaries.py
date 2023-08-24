#!/usr/bin/python3
"""Print a user and their completed tasks"""
import json
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(user_url)

    user_json = user.json()

    all_dicts = {
            }

    for i in user_json:
        todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
                   .format(i['id'])
        todos = requests.get(todo_url)
        todo = todos.json()
        all_dicts[i['id']] = []
        for j in range(0, len(todo)):
            all_dicts[i['id']].append({"username": i['username'],
                                       "task": todo[j]["title"],
                                       "completed": todo[j]["completed"]})

    with open("todo_all_employees.json", 'w') as f:
        f.write(json.dumps(all_dicts))
