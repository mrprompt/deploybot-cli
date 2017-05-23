# -*- coding: utf-8 -*-
from .client import Client


"""
Repository Class
"""


class Repository(Client):
    """
    List repositories
    :return string
    """
    def list(self):
        return super(Repository, self)\
            .get("repositories")

    """
    Get repository
    :return string
    """
    def get(self, repository):
        return super(Repository, self)\
            .get("repositories/%s" % repository)
