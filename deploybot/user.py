# -*- coding: utf-8 -*-
from .client import Client


class User(Client):
    def list(self):
        return super(User, self).get("users")

    def get(self, user):
        return super(User, self).get("users/%s" % user)
