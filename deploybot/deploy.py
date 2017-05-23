# -*- coding: utf-8 -*-
from .client import Client


"""
Deployment Class
"""


class Deploy(Client):
    """
    List deployments
    :return string
    """
    def list(self, repository="", environment=""):
        url = "deployments?limit=20&repository_id=%s&environment_id=%s" % \
              (repository, environment)

        return super(Deploy, self).get(url)

    """
    Get deployment by id
    :return string
    """
    def get(self, deploy):
        return super(Deploy, self).get("deployments/%s" % deploy)

    """
    Trigger a deploy
    :return string
    """
    def trigger(self, environment):
        return super(Deploy, self).post("deployments", {'environment_id': environment})
