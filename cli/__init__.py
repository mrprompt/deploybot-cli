#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploybot.client import Client
from deploybot.deploy import Deploy
from deploybot.user import User
from deploybot.repository import Repository
from deploybot.environment import Environment
from deploybot.server import Server
from .help import Help

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
            item['id'],
            item['name'],
            item['title'],
        ]
    elif command == "repository" and cmd == "get":
        body = [
            item[7],
            item[0],
            item[2],
        ]
    elif command == "user" and cmd == "list":
        body = [
            item['id'],
            item['first_name'] + ' ' + item['last_name'],
            item['email'],
            item['is_admin'],
        ]
    elif command == "user" and cmd == "get":
        body = [
            item[7],  # id
            item[0] + ' ' + item[1],  # name
            item[4],  # email
            bool(item[5]),  # admin
        ]
    elif command == "environment" and cmd == "list":
        body = [
            item['id'],
            item['repository_id'],
            item['name'],
            item['branch_name'],
            item['is_automatic'],
            item['current_version'],
        ]
    elif command == "environment" and cmd == "get":
        body = [
            item[10],
            item[0],
            item[1],
            item[7],
            item[6],
            item[9],
        ]
    elif command == "deploy" and cmd == "list":
        body = [
            item['id'],
            item['repository_id'],
            item['environment_id'],
            item['state'],
            item['deployed_version'],
        ]
    elif command == "deploy" and cmd == "get":
        body = [
            item[13],
            item[1],
            item[2],
            item[10],
            item[11],
        ]
    elif command == "deploy" and cmd == "trigger":
        body = [
            item[13],
            item[1],
            item[2],
            item[10],
            item[11],
        ]
    elif command == "server" and cmd == "list":
        body = [
            item['id'],
            item['environment_id'],
            item['name'],
            item['protocol'],
        ]
    elif command == "server" and cmd == "get":
        body = [
            item[8],
            item[1],
            item[3],
            item[2],
        ]
    elif command == "help":
        body = [
            item['command'],
            item['description'],
            item['params']
        ]
    else:
        raise IndexError("Body not found")

    return body


def response(cmd, param, result):
    content = json.loads(result)
    data = []

    if param == 'list':
        items = content.items()

        for item in items[1][1]:
            data.append(body(cmd, param, item))
    else:
        item = content.values()

        data.append(body(cmd, param, item))

    return data


def main(out=sys.stdout):
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
        data = response(arg1, cmd, result)
    except Exception as e:
        header = ('Error', 'Code')
        data = [
            (
                str(e),
                "try %s help" % sys.argv[0],
            )
        ]

    tableprint.table(data, headers=header, width=int(column_width), style=style, out=out)
