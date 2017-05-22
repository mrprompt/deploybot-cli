# -*- coding: utf-8 -*-
from .client import Client


class Deploy(Client):
    def list(self, repository="", environment=""):
        url = "deployments?limit=20&repository_id=%s&environment_id=%s" % \
              (repository, environment)

        client = self.get_client(url)
        response = client.get()

        return response.body

    def get(self, deploy):
        url = "deployments/%s" % deploy

        client = self.get_client(url)
        response = client.get()

        return response.body

    def trigger(self, environment):
        url = "deployments"

        client = self.get_client(url)
        response = client.post(request_body={'environment_id': environment})

        return response.body
