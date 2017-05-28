from deploybot.environment import Environment
from .config import Config

import click
import tableprint

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group('environment', short_help='Environment commands')
def environment():
    pass


@environment.command('list')
@click.argument('repository', type=int, required=False)
@pass_config
def environment_list(config, repository=None):
    """List environments"""
    client = Environment(config.client)
    result = client.list(repository)
    header = ('ID', 'Repository ID', 'Environment Name', 'Branch', 'Automatic', 'Current')
    # data = response('environment', 'list', result)

    # tableprint.table(data, headers=header, width=int(config.width), style=config.style)
    click.echo(result)


@environment.command('get')
@click.argument('id', type=int)
@pass_config
def environment_get(config, id):
    """Get info from environment"""
    client = Environment(config.client)
    result = client.get(id)
    header = ('ID', 'Repository ID', 'Environment Name', 'Branch', 'Automatic', 'Current')

    click.echo(result)