#!/usr/bin/python3
"""
Python script that retrieves tasks for each employee from a REST API.
"""

import json
import requests

def main():
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users"
    todo_endpoint = f"{base_url}/todos"

    response_users = requests.get(user_endpoint)
    response_todos = requests.get(todo_endpoint)

    users_data = response_users.json()
    todos_data = response_todos.json()

    employee_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        tasks = [{"username": username,
                  "task": task["title"],
                  "completed": task["completed"]}
                 for task in todos_data if task["userId"] == user_id]

        employee_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(employee_tasks, jsonfile, indent=4)

if __name__ == "__main__":
    main()
