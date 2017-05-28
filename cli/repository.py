from deploybot.repository import Repository
from .config import Config

import click
import tableprint

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group('repository', short_help='Repository commands')
def repository():
    pass


@repository.command('list')
@pass_config
def repository_list(config):
    """List repositorys"""
    client = Repository(config.client)
    result = client.list()
    header = ('ID', 'Title', 'Name')
    # data = response('repository', 'list', result)

    # tableprint.table(data, headers=header, width=int(config.width), style=config.style)
    click.echo(result)


@repository.command('get')
@click.argument('id', type=int)
@pass_config
def repository_get(config, id):
    """Get info from repository"""
    client = Repository(config.client)
    result = client.get(id)
    header = ('ID', 'Title', 'Name')

    click.echo(result)