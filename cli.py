#!/usr/bin/env python
from deploybot.deploy import Deploy
from deploybot.user  import User
from deploybot.repository import Repository
from deploybot.environment import Environment
import sys
import json
import tableprint


def run(command):
    if command == "repository":
        client = Repository()
    elif command == "user":
        client = User()
    elif command == "environment":
        client = Environment()
    elif command == "deploy":
        client = Deploy()
    else:
        raise IndexError("Command not found")

    return client

def headers(command):
    if command == "repository":
        headers = ('ID', 'Title', 'Name')
    elif command == "user":
        headers = ('ID', 'Name', 'Email', 'Admin')
    elif command == "environment":
        headers = ('ID', 'Repository ID', 'Environment Name')
    elif command == "deploy":
        headers = ('ID', 'Repository ID', 'Environment ID', 'State')
    else:
        raise IndexError("Header not found")

    return headers

def body(command, item):
    if command == "repository":
        body = [
            unicode(item['id']),
            unicode(item['name']),
            unicode(item['title']),
        ]
    elif command == "user":
        body = [
            unicode(item['id']),
            unicode(item['first_name'] + ' ' + item['last_name']),
            unicode(item['email']),
            unicode(item['is_admin']),
        ]
    elif command == "environment":
        body = [
            unicode(item['id']),
            unicode(item['repository_id']),
            unicode(item['name']),
        ]
    elif command == "deploy":
        body = [
            unicode(item['id']),
            unicode(item['repository_id']),
            unicode(item['environment_id']),
            unicode(item['state']),
        ]
    else:
        raise IndexError("Body not found")

    return body

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
        result = run(arg1).list()
        jsonObject = json.loads(result)
        items = jsonObject.items()
        data = []

        for item in items[1][1]:
            data.append(body(arg1, item))

        tableprint.table(data, headers=headers(arg1), width=32, style="fancy_grid")

    except IndexError as e:
        print(str(e))
