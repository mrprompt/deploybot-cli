from deploybot.server import Server
from .config import Config

import click
import tableprint

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group('server', short_help='Server commands')
def server():
    pass


@server.command('list')
@pass_config
def server_list(config):
    """List servers"""
    client = Server(config.client)
    result = client.list()
    header = ('ID', 'Environment ID', 'Name', 'Protocol')
    # data = response('server', 'list', result)

    # tableprint.table(data, headers=header, width=int(config.width), style=config.style)
    click.echo(result)


@server.command('get')
@click.argument('id', type=int)
@pass_config
def server_get(config, id):
    """Get info from server"""
    client = Server(config.client)
    result = client.get(id)
    header = ('ID', 'Environment ID', 'Name', 'Protocol')

    click.echo(result)