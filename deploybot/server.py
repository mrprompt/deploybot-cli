# -*- coding: utf-8 -*-
from .client import Client


class Server(Client):
    def list(self):
        params = {
            "query_params": {
                "limit": 20
            }
        }

        client = self.get_client("servers")
        response = client.get(params)

        return response.body
