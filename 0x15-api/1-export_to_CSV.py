#!/usr/bin/python3

"""
A python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for ui in data2:
        if ui['id'] == int(argv[1]):
            employee = ui['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for ui in data:

            row = []
            if ui['userId'] == int(argv[1]):
                row.append(ui['userId'])
                row.append(employee)
                row.append(ui['completed'])
                row.append(ui['title'])

                writ.writerow(row)
