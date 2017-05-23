# -*- coding: utf-8 -*-
import python_http_client
import os


class Client(object):
    """
    Get url from account
    :return string
    """
    def get_url(self, account="", endpoint=""):
        default_url = "https://%s.deploybot.com/api/v1/%s"

        return default_url % (account, endpoint)

    """
    Get default client
    :return object
    """
    def get_client(self, endpoint=""):
        account = os.environ.get('DEPLOYBOT_ACCOUNT')
        token = os.environ.get('DEPLOYBOT_TOKEN')
        url = self.get_url(account, endpoint)
        headers = {
            "X-Api-Token": token,
        }

        return python_http_client.Client(host=url, request_headers=headers)

    """
    Sent a GET request
    :return string
    """
    def get(self, endpoint):
        response = self.get_client(endpoint).get()

        return response.body

    """
    Sent a POST request
    :return string
    """
    def post(self, endpoint, params):
        response = self.get_client(endpoint).post(request_body=params)

        return response.body
