# -*- coding: utf-8 -*-
"""
Environment Class
"""


class Environment:
    """
    Constructor
    """
    def __init__(self, client):
        self.client = client

    """
    List environments
    :return string
    """
    def list(self, repository=""):
        url = "environments?repository_id=%s" % repository

        return self.client.get(url)

    """
    Get an environment
    :return string
    """
    def get(self, environment):
        url = "environments/%s" % environment

        return self.client.get(url)
