#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Récupérer les données de tous les utilisateurs depuis l'API
    user_data = requests.get(f"{API_URL}/users").json()

    # Créer un dictionnaire pour stocker les données de tous les employés
    all_employee_data = {}

    # Parcourir chaque user pour obtenir ses tâches et les stocker dans le dict
    for user in user_data:
        user_id = str(user['id'])
        tasks_data = requests.get(f"{API_URL}/todos?userId={user_id}").json()

        # Préparer les données des tâches pour l'utilisateur actuel
        tasks_info = [
            {"username": user['username'],
                "task": task['title'],
                "completed": task['completed']}
            for task in tasks_data
        ]

        all_employee_data[user_id] = tasks_info

    # Écrire les données dans un fichier JSON
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_employee_data, json_file)
