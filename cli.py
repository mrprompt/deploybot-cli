#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deploybot.client import Client

if __name__ == "__main__":
    client = Client()

    print(client.getUrl("mrprompt"))