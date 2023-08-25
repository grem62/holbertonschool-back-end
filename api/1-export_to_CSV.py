#!/usr/bin/python3
"""Script to export data in the CSV format"""
import requests
import csv
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Récupérer l'ID de l'employé depuis les args de ligne de commande
    employee_id = argv[1]

    # Obtenir les informations sur l'utilisateur depuis l'API
    user_data = requests.get(f"{API_URL}/users/{employee_id}").json()

    # Obtenir la liste des tâches à faire pour l'employé depuis l'API
    todo_data = requests.get(f"{API_URL}/todos?userId={employee_id}").json()

    # Write to CSV file
    with open(f"{employee_id}.csv", mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            writer.writerow([
                user_data['id'],
                user_data['username'],
                task['completed'],
                task['title']
            ])

    print(f"Data has been exported to {employee_id}.csv")
