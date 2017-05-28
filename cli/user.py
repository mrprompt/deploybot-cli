from deploybot.user import User
from .config import Config

import click
import tableprint

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group('user', short_help='User account commands')
def user():
    pass


@user.command('list')
@pass_config
def user_list(config):
    """List all users from account"""
    client = User(config.client)
    result = client.list()
    header = ('ID', 'Name', 'Email', 'Admin')
    # data = response('user', 'list', result)

    # tableprint.table(data, headers=header, width=int(config.width), style=config.style)
    click.echo(result)


@user.command('get')
@click.argument('id')
@pass_config
def user_get(config, id):
    """Get info from user"""
    client = User(config.client)
    result = client.get(id)
    header = ('ID', 'Name', 'Email', 'Admin')
    # data = response('user', 'list', result)

    # tableprint.table(data, headers=header, width=int(config.width), style=config.style)
    click.echo(result)
