from deploybot.user import User
from .config import Config
from . import response
from io import StringIO
import click
import tableprint

output = StringIO()
pass_config = click.make_pass_decorator(Config, ensure=True)
header = ('ID', 'Name', 'Email', 'Admin')


@click.group('user', short_help='User account commands')
def user():
    pass


@user.command('list')
@pass_config
def user_list(config):
    """List all users from account"""
    client = User(config.client)
    result = client.list()
    data = response('user', 'list', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())


@user.command('get')
@click.argument('id')
@pass_config
def user_get(config, id):
    """Get info from user"""
    client = User(config.client)
    result = client.get(id)
    data = response('user', 'get', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())
