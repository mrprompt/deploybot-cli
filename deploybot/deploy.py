# -*- coding: utf-8 -*-
from .client import Client


class Deploy(Client):
    def list(self, repository="", environment=""):
        url = "deployments?limit=20&repository_id=%s&environment_id=%s" % \
              (repository, environment)
        client = self.get_client(url)
        response = client.get()

        return response.body
