# -*- coding: utf-8 -*-
from .client import Client


class Repository(Client):
    def list(self):
        params = {
            "query_params": {
                "limit": 20
            }
        }

        client = self.get_client("repositories")
        response = client.get(params)

        return response.body
