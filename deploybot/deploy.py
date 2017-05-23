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
        url = "deployments?limit=20&repository_id=%s&environment_id=%s" % (repository, environment)

        return super(Deploy, self).get(url)

    """
    Get deployment by id
    :return string
    """
    def get(self, deploy):
        url = "deployments/%s" % deploy

        return super(Deploy, self).get(url)

    """
    Trigger a deploy
    :return string
    """
    def trigger(self, environment):
        args = ("deployments", {'environment_id': environment})

        return super(Deploy, self).post(*args)
