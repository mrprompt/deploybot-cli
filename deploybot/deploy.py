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
        url = "deployments?limit=20"
        url += "&repository_id=%s" % repository
        url += "&environment_id=%s" % environment

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
