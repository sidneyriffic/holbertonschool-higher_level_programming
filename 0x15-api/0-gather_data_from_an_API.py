#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""


if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get("http://jsonplaceholder.typicode.com/users/"
                        + argv[1]).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId="
                         + argv[1]).json()
    done = requests.get("http://jsonplaceholder.typicode.com/todos?userId="
                        + argv[1] + "&completed=true").json()

    print("Employee {} is done with tasks({}/{})"
          .format(user["name"], len(done), len(todos)))
    for task in done:
        print("\t" + task["title"])
