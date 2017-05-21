# -*- coding: utf-8 -*-
from .client import Client


class Deploy(Client):
    def list(self, repository=""):
        params = {
            "query_params": {
                "limit": 20,
                "repository_id": repository
            }
        }

        client = self.get_client("deployments")
        response = client.get(params)

        return response.status_code
