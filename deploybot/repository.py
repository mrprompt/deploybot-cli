# -*- coding: utf-8 -*-
from .client import Client


class Repository(Client):
    def list(self):
        return super(Repository, self).get("repositories")

    def get(self, repository):
        return super(Repository, self).get("repositories/%s" % repository)
