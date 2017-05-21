#!/usr/bin/env python
from deploybot.repository import Repository
import sys

if __name__ == "__main__":
    client = Repository()
    arg1 = sys.argv[1]

    result = client.list()

    print(result)