#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploybot.deploy import Deploy
from deploybot.user  import User
from deploybot.repository import Repository
from deploybot.environment import Environment
from deploybot.server import Server
from deploybot.help import Help
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
    elif command == "help":
        client = Help()
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
    elif command == "help":
        headers = ('Command', 'Description', 'Parameters')
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
    elif command == "help":
        body = [
            unicode(item['command']),
            unicode(item['description']),
            unicode(item['params'])
        ]
    else:
        raise IndexError("Body not found")

    return body


def main():
    column_width = os.environ.get('COLUMN_WIDTH', 32)

    try:
        arg1 = sys.argv[1]

        args = copy.copy(sys.argv)

        args.pop(0)
        args.pop(0)

        header = headers(arg1)
        result = run(arg1).list(*args)
        jsonObject = json.loads(result)

        items = jsonObject.items()
        # print(items[1][1])
        data = []

        for item in items[1][1]:
            data.append(body(arg1, item))
    except TypeError as e:
        header = ('Error', 'Code')
        data = [str(e), 0]
    except IndexError as e:
        header = ('Error', 'Code')
        data = [
            (
                str(e),
                "try %s help" % sys.argv[0],
            )
        ]

    tableprint.table(data, headers=header, width=int(column_width), style="fancy_grid")


if __name__ == "__main__":
    main()
