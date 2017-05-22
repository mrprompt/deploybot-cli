# -*- coding: utf-8 -*-
from .client import Client


class Environment(Client):
    def list(self, repository=""):
        url = "environments?repository_id=%s" % repository
        client = self.get_client(url)
        response = client.get()

        return response.body
