import os
from deploybot.client import Client


class Config(object):

    def __init__(self):
        self.account = os.environ.get('DEPLOYBOT_ACCOUNT')
        self.token = os.environ.get('DEPLOYBOT_TOKEN')
        self.width = os.environ.get('COLUMN_WIDTH', 32)
        self.style = os.environ.get('COLUMN_STYLE', 'fancy_grid')
        self.client = Client(self.account, self.token)