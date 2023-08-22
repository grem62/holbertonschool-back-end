#!/usr/bin/python

import requests
from sys import argv
import json

url_ap = "https://jsonplaceholder.typicode.com"


def api():
    user_response = requests.get(f"{url_ap}/users/{argv[1]}").json()
    todo_response = requests.get(f"{url_ap}/todos?userId={argv[1]}").json()
    filtrer_task = [task for task in todo_response if task["completed"]]

    employee_name = user_response["name"]
    num_completed_tasks = len(todo_response)
    total_tasks = len(todo_response)
    print("Employee {} is done with tasks({}/{}):".format(
      employee_name, num_completed_tasks, total_tasks))
    for task in filtrer_task:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    api()
