from deploybot.server import Server
from .config import Config
from . import response
from io import StringIO
import click
import tableprint

output = StringIO()
pass_config = click.make_pass_decorator(Config, ensure=True)
header = ('ID', 'Environment ID', 'Name', 'Protocol')


@click.group('server', short_help='Server commands')
def server():
    pass


@server.command('list')
@pass_config
def server_list(config):
    """List servers"""
    client = Server(config.client)
    result = client.list()
    data = response('server', 'list', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())


@server.command('get')
@click.argument('id', type=int)
@pass_config
def server_get(config, id):
    """Get info from server"""
    client = Server(config.client)
    result = client.get(id)
    data = response('server', 'get', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())
