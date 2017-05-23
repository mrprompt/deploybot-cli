# -*- coding: utf-8 -*-
"""
Server Class
"""


class Server:
    """
    Constructor
    """
    def __init__(self, client):
        self.client = client

    """
    List servers
    :return string
    """
    def list(self):
        url = "servers"

        return self.client.get(url)

    """
    Get server
    :return string
    """
    def get(self, server):
        url = "servers/%s" % server

        return self.client.get(url)
