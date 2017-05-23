# -*- coding: utf-8 -*-
from .client import Client


class Environment(Client):
    def list(self, repository=""):
        return super(Environment, self).get("environments?repository_id=%s" % repository)

    def get(self, environment):
        return super(Environment, self).get("environments/%s" % environment)
