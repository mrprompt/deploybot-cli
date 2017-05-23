# -*- coding: utf-8 -*-
"""
Repository Class
"""


class Repository:
    """
    Constructor
    """
    def __init__(self, client):
        self.client = client

    """
    List repositories
    :return string
    """
    def list(self):
        url = "repositories"

        return self.client.get(url)

    """
    Get repository
    :return string
    """
    def get(self, repository):
        url = "repositories/%s" % repository

        return self.client.get(url)
