#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploybot.client import Client
from deploybot.deploy import Deploy
from deploybot.user import User
from deploybot.repository import Repository
from deploybot.environment import Environment
from deploybot.server import Server
from deploybot.help import Help
import json
import tableprint
import copy
import os
import sys


def run(command):
    account = os.environ.get('DEPLOYBOT_ACCOUNT')
    token = os.environ.get('DEPLOYBOT_TOKEN')
    client = Client(account, token)

    if command == "repository":
        client = Repository(client)
    elif command == "user":
        client = User(client)
    elif command == "environment":
        client = Environment(client)
    elif command == "deploy":
        client = Deploy(client)
    elif command == "server":
        client = Server(client)
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
        headers = ('ID', 'Repository ID', 'Environment Name', 'Branch', 'Automatic', 'Current')
    elif command == "deploy":
        headers = ('ID', 'Repository ID', 'Environment ID', 'State', 'Version')
    elif command == "server":
        headers = ('ID', 'Environment ID', 'Name', 'Protocol')
    elif command == "help":
        headers = ('Command', 'Description', 'Parameters')
    else:
        raise IndexError("Header not found")

    return headers


def body(command, cmd, item):
    if command == "repository" and cmd == "list":
        body = [
            unicode(item['id']),
            unicode(item['name']),
            unicode(item['title']),
        ]
    elif command == "repository" and cmd == "get":
        body = [
            unicode(item[7]),
            unicode(item[0]),
            unicode(item[2]),
        ]
    elif command == "user" and cmd == "list":
        body = [
            unicode(item['id']),
            unicode(item['first_name'] + ' ' + item['last_name']),
            unicode(item['email']),
            unicode(item['is_admin']),
        ]
    elif command == "user" and cmd == "get":
        body = [
            unicode(item[7]),  # id
            unicode(item[0] + ' ' + item[1]),  # name
            unicode(item[4]),  # email
            unicode(bool(item[5])),  # admin
        ]
    elif command == "environment" and cmd == "list":
        body = [
            unicode(item['id']),
            unicode(item['repository_id']),
            unicode(item['name']),
            unicode(item['branch_name']),
            unicode(item['is_automatic']),
            unicode(item['current_version']),
        ]
    elif command == "environment" and cmd == "get":
        body = [
            unicode(item[10]),
            unicode(item[0]),
            unicode(item[1]),
            unicode(item[7]),
            unicode(item[6]),
            unicode(item[9]),
        ]
    elif command == "deploy" and cmd == "list":
        body = [
            unicode(item['id']),
            unicode(item['repository_id']),
            unicode(item['environment_id']),
            unicode(item['state']),
            unicode(item['deployed_version']),
        ]
    elif command == "deploy" and cmd == "get":
        body = [
            unicode(item[13]),
            unicode(item[1]),
            unicode(item[2]),
            unicode(item[10]),
            unicode(item[11]),
        ]
    elif command == "deploy" and cmd == "trigger":
        body = [
            unicode(item[13]),
            unicode(item[1]),
            unicode(item[2]),
            unicode(item[10]),
            unicode(item[11]),
        ]
    elif command == "server" and cmd == "list":
        body = [
            unicode(item['id']),
            unicode(item['environment_id']),
            unicode(item['name']),
            unicode(item['protocol']),
        ]
    elif command == "server" and cmd == "get":
        body = [
            unicode(item[8]),
            unicode(item[1]),
            unicode(item[3]),
            unicode(item[2]),
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
    style = os.environ.get('COLUMN_STYLE', 'fancy_grid')

    try:
        arg1 = sys.argv[1]

        args = copy.copy(sys.argv)

        args.pop(0)
        args.pop(0)

        if arg1 == 'help':
            cmd = 'list'
        else:
            cmd = args.pop(0)

        result = getattr(run(arg1), cmd)(*args)

        header = headers(arg1)
        content = json.loads(result)
        data = []

        if cmd == 'list':
            items = content.items()

            for item in items[1][1]:
                data.append(body(arg1, cmd, item))
        else:
            item = content.values()

            data.append(body(arg1, cmd, item))

    except Exception as e:
        header = ('Error', 'Code')
        data = [
            (
                str(e),
                "try %s help" % sys.argv[0],
            )
        ]

    tableprint.table(data, headers=header, width=int(column_width), style=unicode(style))


if __name__ == "__main__":
    main()
