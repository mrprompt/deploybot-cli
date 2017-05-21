# -*- coding: utf-8 -*-

class Client(object):
    """
    Get url from account
    :return string
    """
    def getUrl(self, account):
        default_url = "https://%s.deploybot.com/api/v1"

        return default_url % account