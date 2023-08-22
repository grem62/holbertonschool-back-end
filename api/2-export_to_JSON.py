#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv
import csv
import json

url_ap = "https://jsonplaceholder.typicode.com"


def api():
    # information user
    user_response = requests.get(f"{url_ap}/users/{argv[1]}").json()
    # liste des choses a faire pour le user
    todo_response = requests.get(f"{url_ap}/todos?userId={argv[1]}").json()

    data = {
        argv[1]: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_response['username']
            }
            for task in todo_response
        ]
    }

    # Write to JSON file
    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        jsonfile.write(json.dumps(data))
        jsonfile.close()


if __name__ == "__main__":
    api()
