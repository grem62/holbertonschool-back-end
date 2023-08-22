#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv
import csv
url_ap = "https://jsonplaceholder.typicode.com"


def api():
    # information user
    user_response = requests.get(f"{url_ap}/users/{argv[1]}").json()
    # liste des choses a faire pour le user
    todo_response = requests.get(f"{url_ap}/todos?userId={argv[1]}").json()
    # écrire au format CSV
    with open(f"{argv[1]}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_response:
            writer.writerow([
                user_response['id'],
                user_response['username'],
                task['completed'],
                task['title']
            ])


if __name__ == "__main__":
    api()
