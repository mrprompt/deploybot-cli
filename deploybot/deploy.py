# -*- coding: utf-8 -*-
from .client import Client


class Deploy(Client):
    def list(self, repository="", environment=""):
        params = {
            "query_params": {
                "limit": 20,
                "repository_id": repository,
                "environment_id": environment
            }
        }

        client = self.get_client("deployments")
        response = client.get(params)

        return response.status_code
