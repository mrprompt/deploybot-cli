# -*- coding: utf-8 -*-
from .client import Client


class Server(Client):
    def list(self):
        client = self.get_client("servers")
        response = client.get()

        return response.body
