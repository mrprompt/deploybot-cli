# -*- coding: utf-8 -*-
from .client import Client


class Server(Client):
    def list(self):
        return super(Server, self).get("servers")

    def get(self, server):
        return super(Server, self).get("servers/%s" % server)
