# -*- coding: utf-8 -*-
from .client import Client

"""
User Class
"""


class User(Client):
    """
    List users
    :return string
    """
    def list(self):
        return super(User, self)\
            .get("users")

    """
    Get user
    :return string
    """
    def get(self, user):
        return super(User, self)\
            .get("users/%s" % user)
