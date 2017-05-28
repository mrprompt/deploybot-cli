from deploybot.environment import Environment
from .config import Config
from . import response
from io import StringIO
import click
import tableprint

output = StringIO()
pass_config = click.make_pass_decorator(Config, ensure=True)
header = ('ID', 'Repository ID', 'Environment Name', 'Branch', 'Automatic', 'Current')


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
    data = response('environment', 'list', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())


@environment.command('get')
@click.argument('id', type=int)
@pass_config
def environment_get(config, id):
    """Get info from environment"""
    client = Environment(config.client)
    result = client.get(id)
    data = response('environment', 'get', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())
