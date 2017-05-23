# -*- coding: utf-8 -*-
"""
Deployment Class
"""


class Deploy:
    """
    Constructor
    """
    def __init__(self, client):
        self.client = client

    """
    List deployments
    :return string
    """
    def list(self, repository="", environment=""):
        url = "deployments?limit=20"
        url += "&repository_id=%s" % repository
        url += "&environment_id=%s" % environment

        return self.client.get(url)

    """
    Get deployment by id
    :return string
    """
    def get(self, deploy):
        url = "deployments/%s" % deploy

        return self.client.get(url)

    """
    Trigger a deploy
    :return string
    """
    def trigger(self, environment):
        args = ("deployments", {'environment_id': environment})

        return self.client.post(*args)
