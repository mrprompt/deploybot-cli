#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploybot.deploy import Deploy
from deploybot.user  import User
from deploybot.repository import Repository
from deploybot.environment import Environment
from deploybot.server import Server
import sys
import json
import tableprint
import copy
import os


def run(command):
    if command == "repository":
        client = Repository()
    elif command == "user":
        client = User()
    elif command == "environment":
        client = Environment()
    elif command == "deploy":
        client = Deploy()
    elif command == "server":
        client = Server()
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
    elif command == "server":
        headers = ('ID', 'Environment ID', 'Name', 'Protocol')
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
    elif command == "server":
        body = [
            unicode(item['id']),
            unicode(item['environment_id']),
            unicode(item['name']),
            unicode(item['protocol']),
        ]
    else:
        raise IndexError("Body not found")

    return body


def main():
    column_width = os.environ.get('COLUMN_WIDTH', 32)

    try:
        arg1 = sys.argv[1]

        if arg1 != '--help':
            args = copy.copy(sys.argv)

            args.pop(0)
            args.pop(0)

            header = headers(arg1)
            result = run(arg1).list(*args)
            jsonObject = json.loads(result)

            items = jsonObject.items()
            data = []

            for item in items[1][1]:
                data.append(body(arg1, item))
        else:
            header = ('Command', 'Description', 'Parameters')
            data = [
                (
                    'user',
                    'list users',
                    ''
                ),
                (
                    'deploy',
                    'list deployments',
                    '[repository_id] [environment_id]'
                ),
                (
                    'environment',
                    'list environments',
                    '[repository_id]'
                ),
                (
                    'repository',
                    'list repositories',
                    ''
                ),
                (
                    'server',
                    'list servers',
                    '[repository_id] [environment_id]'
                )
            ]

        tableprint.table(data, headers=header, width=int(column_width), style="fancy_grid")

    except TypeError as e:
        print(str(e))

    except IndexError as e:
        print("try %s --help" % sys.argv[0])


if __name__ == "__main__":
    main()
