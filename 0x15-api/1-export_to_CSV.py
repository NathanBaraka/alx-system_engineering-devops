#!/usr/bin/python3
"""Export to-do list information for a specific employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Retrieve the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information from the API and
    #   parse the response as a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Retrieve the to-do list items associated with the
    #   provided user ID and parse the response as a JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Utilize list comprehension to iterate over the to-do list items
    # Write each item's details (user ID, username, completion status,
    #   and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
