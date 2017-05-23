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
        return super(Environment, self).get("environments?repository_id=%s" % repository)

    """
    Get an environment
    :return string
    """
    def get(self, environment):
        return super(Environment, self).get("environments/%s" % environment)
