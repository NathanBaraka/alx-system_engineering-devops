#!/usr/bin/python3
"""
This script gathers employee data from an API.
"""

import requests
import sys
import re


def get_employee_data(employee_id):
    """
    Get the employee data from the API.
    """
    url = "{}/users/{}".format(REST_API, employee_id)
    return requests.get(url).json()


def get_tasks_data():
    """
    Get the tasks data from the API.
    """
    url = "{}/todos".format(REST_API)
    return requests.get(url).json()


def get_employee_name(employee_data):
    """
    Get the employee name.
    """
    return employee_data.get('name')


def get_tasks_for_employee(employee_id, tasks_data):
    """
    Get the tasks for the employee.
    """
    return list(filter(lambda x: x.get('userId') == employee_id, tasks_data))


def get_completed_tasks_for_employee(tasks):
    """
    Get the completed tasks for the employee.
    """
    return list(filter(lambda x: x.get('completed'), tasks))


def print_tasks(tasks):
    """
    Print the completed tasks.
    """
    for task in tasks:
        print('\t {}'.format(task.get('title')))


REST_API = "https://jsonplaceholder.typicode.com"


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        if re.fullmatch(r'\d+', str(employee_id)):
            employee_data = get_employee_data(employee_id)
            tasks_data = get_tasks_data()
            employee_name = get_employee_name(employee_data)
            tasks = get_tasks_for_employee(employee_id, tasks_data)
            completed_tasks = get_completed_tasks_for_employee(tasks)
            print('Employee {} is done with tasks({}/{}):'.format(
                employee_name, len(completed_tasks), len(tasks)))
            if len(completed_tasks) > 0:
                print_tasks(completed_tasks)


if __name__ == '__main__':
    main()
