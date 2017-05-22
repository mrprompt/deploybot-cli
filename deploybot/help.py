# -*- coding: utf-8 -*-
from .client import Client
import json


class Help(Client):
    def list(self):
        content = {
            'meta': {
                'total': 7
            },
            'entries': [
                {
                    'command': 'user',
                    'description': 'list users',
                    'params': ''
                },
                {
                    'command': 'deploy',
                    'description': 'list deployments',
                    'params': '[repository_id] [environment_id]'
                },
                {
                    'command': 'environment',
                    'description': 'list environments',
                    'params': '[repository_id]'
                },
                {
                    'command': 'repository',
                    'description': 'list repositories',
                    'params': ''
                },
                {
                    'command': 'server',
                    'description': 'list servers',
                    'params': '[repository_id] [environment_id]'
                }
            ]
        }

        result = json.dumps(content)

        # print(result)
        return result
