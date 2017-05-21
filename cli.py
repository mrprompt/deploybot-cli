#!/usr/bin/env python
from deploybot.deploy import Deploy
from deploybot.user  import User
from deploybot.repository import Repository
from deploybot.environment import Environment
import sys


def run(command):
    client = object

    if command == "repository":
        client = Repository()
    elif command == "user":
        client = User()
    elif command == "repository":
        client = Repository()
    elif command == "environment":
        client = Environment()
    elif command == "deploy":
        client = Deploy()
    else:
        raise IndexError("Command not found")

    return client

if __name__ == "__main__":

    try:
        arg1 = sys.argv[1]
        result = run(arg1).list()

        print(result)
    except IndexError as e:
        print "--help"
