# -*- coding: utf-8 -*-
from .client import Client


class Environment(Client):
    def list(self, repository=""):
        params = {
            "query_params": {
                "limit": 20,
                "repository_id": repository
            }
        }

        client = self.get_client("environments")
        response = client.get(params)

        return response.status_code
