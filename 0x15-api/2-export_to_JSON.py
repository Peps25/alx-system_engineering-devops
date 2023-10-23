#!/usr/bin/python3

"""
A python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for ui in data2:
        if ui['id'] == int(argv[1]):
            u_name = ui['username']
            id_no = ui['id']

    row = []

    for ui in data:

        new_dict = {}

        if ui['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = ui['title']
            new_dict['completed'] = ui['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
