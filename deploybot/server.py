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
        return super(Server, self).get("servers")

    """
    Get server
    :return string
    """
    def get(self, server):
        return super(Server, self).get("servers/%s" % server)
