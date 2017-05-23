# -*- coding: utf-8 -*-
from .client import Client

"""
Server Class
"""


class Server(Client):
    """
    List servers
    :return string
    """
    def list(self):
        url = "servers"

        return super(Server, self).get(url)

    """
    Get server
    :return string
    """
    def get(self, server):
        url = "servers/%s" % server

        return super(Server, self).get(url)
