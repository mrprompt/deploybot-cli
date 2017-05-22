# -*- coding: utf-8 -*-
from json import dumps


class Help(object):
    def list(self):
        content = {
            'meta': {
                'total': 7
            },
            'entries': [
                {
                    'command': 'user list',
                    'description': 'list users',
                    'params': ''
                },
                {
                    'command': 'deploy list',
                    'description': 'list deployments',
                    'params': '[repository_id] [environment_id]'
                },
                {
                    'command': 'environment list',
                    'description': 'list environments',
                    'params': '[repository_id]'
                },
                {
                    'command': 'repository list',
                    'description': 'list repositories',
                    'params': ''
                },
                {
                    'command': 'server list',
                    'description': 'list servers',
                    'params': '[repository_id] [environment_id]'
                }
            ]
        }

        result = dumps(content)

        return result
