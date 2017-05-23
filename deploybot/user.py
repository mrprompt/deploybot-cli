# -*- coding: utf-8 -*-
"""
User Class
"""


class User:
    """
    Constructor
    """
    def __init__(self, client):
        self.client = client

    """
    List users
    :return string
    """
    def list(self):
        return self.client.get("users")

    """
    Get user
    :return string
    """
    def get(self, user):
        return self.client.get("users/%s" % user)
