from deploybot.repository import Repository
from .config import Config
from . import response
from io import StringIO
import click
import tableprint

output = StringIO()
pass_config = click.make_pass_decorator(Config, ensure=True)
header = ('ID', 'Title', 'Name')


@click.group('repository', short_help='Repository commands')
def repository():
    pass


@repository.command('list')
@pass_config
def repository_list(config):
    """List repositorys"""
    client = Repository(config.client)
    result = client.list()
    data = response('repository', 'list', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())


@repository.command('get')
@click.argument('id', type=int)
@pass_config
def repository_get(config, id):
    """Get info from repository"""
    client = Repository(config.client)
    result = client.get(id)
    data = response('repository', 'get', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())
