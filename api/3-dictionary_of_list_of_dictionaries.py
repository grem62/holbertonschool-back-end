#!/usr/bin/python3
"""
description of script
"""
import json
import requests

if __name__ == "__main__":

    URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f'{URL}/users').json()
    dict_user = {}
    for user in users:
        tasks = requests.get(f'{URL}/users/{user["id"]}/todos').json()
        dict_user[user['id']] = []
        for task in tasks:
            dict_task = {"task": task["title"], "completed": task["completed"],
                         "username": user["username"]}
            dict_user[user["id"]].append(dict_task)
    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_user, file)
