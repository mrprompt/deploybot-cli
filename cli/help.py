# -*- coding: utf-8 -*-
from json import dumps

"""
Help Class
"""


class Help(object):
    """
    List help
    :return string
    """
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
                    'command': 'user get',
                    'description': 'get user',
                    'params': '[user_id]'
                },
                {
                    'command': 'deploy list',
                    'description': 'list deployments',
                    'params': '[repository_id] [environment_id]'
                },
                {
                    'command': 'deploy get',
                    'description': 'get deploy',
                    'params': '[deploy_id]'
                },
                {
                    'command': 'deploy trigger',
                    'description': 'trigger deploy',
                    'params': '[deploy_id]'
                },
                {
                    'command': 'environment list',
                    'description': 'list environments',
                    'params': '[repository_id]'
                },
                {
                    'command': 'environment get',
                    'description': 'get environment',
                    'params': '[enviroment_id]'
                },
                {
                    'command': 'repository list',
                    'description': 'list repositories',
                    'params': ''
                },
                {
                    'command': 'repository get',
                    'description': 'get repository',
                    'params': ''
                },
                {
                    'command': 'server list',
                    'description': 'list servers',
                    'params': '[repository_id] [environment_id]'
                },
                {
                    'command': 'server get',
                    'description': 'get server',
                    'params': '[server_id]'
                }
            ]
        }

        result = dumps(content)

        return result
