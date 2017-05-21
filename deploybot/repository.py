# -*- coding: utf-8 -*-
from .client import Client


class Repository(Client):
    def list(self):
        client = self.get_client("repositories")
        response = client.get()

        return response.body
