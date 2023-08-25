#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = f"{base_url}/users"
    todo = f"{base_url}/todos"

    response_user = requests.get(user_id)
    response_todo = requests.get(todo)

    user_data = response_user.json()
    todo_data = response_todo.json()

    data_employee = {}

    for users in user_data:
        user_id = users['id']
        username = users['username']

        tasks = [{"username": username,
                  "task": task["title"],
                  "completed": task["completed"]}
                 for task in todo_data if task["userId"] == user_id]

        data_employee[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_employee, jsonfile, indent=4)
