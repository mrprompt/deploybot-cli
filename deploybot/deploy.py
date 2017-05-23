# -*- coding: utf-8 -*-
from .client import Client


class Deploy(Client):
    def list(self, repository="", environment=""):
        url = "deployments?limit=20&repository_id=%s&environment_id=%s" % \
              (repository, environment)

        return super(Deploy, self).get(url)

    def get(self, deploy):
        return super(Deploy, self).get("deployments/%s" % deploy)

    def trigger(self, environment):
        return super(Deploy, self).post("deployments", {'environment_id': environment})
