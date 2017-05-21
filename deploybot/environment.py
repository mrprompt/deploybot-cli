# -*- coding: utf-8 -*-
from .client import Client
import urllib


class Environment(Client):
    def list(self, repository=""):
        if len(repository):
            params = {
                "repository_id": repository
            }
        else:
            params = {}

        client = self.get_client("environments?" + urllib.urlencode(params))
        response = client.get(params)

        return response.body
