# -*- coding: utf-8 -*-
from .client import Client

"""
Environment Class
"""


class Environment(Client):
    """
    List environments
    :return string
    """
    def list(self, repository=""):
        url = "environments?repository_id=%s" % repository

        return super(Environment, self).get(url)

    """
    Get an environment
    :return string
    """
    def get(self, environment):
        url = "environments/%s" % environment

        return super(Environment, self).get(url)
