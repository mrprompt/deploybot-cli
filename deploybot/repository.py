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
        url = "repositories"

        return super(Repository, self).get(url)

    """
    Get repository
    :return string
    """
    def get(self, repository):
        url = "repositories/%s" % repository

        return super(Repository, self).get(url)
