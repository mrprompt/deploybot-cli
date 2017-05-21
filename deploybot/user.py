# -*- coding: utf-8 -*-
from .client import Client


class User(Client):
    def list(self):
        client = self.get_client("users")
        response = client.get()

        return response.body
