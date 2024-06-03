#!/usr/bin/python3
""" to-do list information for a given employee id."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed = [todo.get("title") for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed), 
                                                          len(todos)))
    [print("\t {}".format(c)) for c in completed]

