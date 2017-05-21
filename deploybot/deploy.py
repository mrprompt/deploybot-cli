# -*- coding: utf-8 -*-
from .client import Client
import urllib


class Deploy(Client):
    def list(self, repository="", environment=""):
        params = {
            "limit": 20,
            "repository_id": repository,
            "environment_id": environment
        }

        client = self.get_client("deployments?" + urllib.urlencode(params))
        response = client.get()

        return response.body
