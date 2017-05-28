from deploybot.deploy import Deploy
from .config import Config

import click
import tableprint

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group('deploy', short_help='Deploy commands')
def deploy():
    pass


@deploy.command('list')
@click.argument('repository', type=int)
@click.argument('environment', type=int)
@pass_config
def deploy_list(config, repository, environment):
    """List deploys"""
    client = Deploy(config.client)
    result = client.list(repository, environment)
    header = ('ID', 'Repository ID', 'Environment ID', 'State', 'Version')
    # data = response('deploy', 'list', result)

    # tableprint.table(data, headers=header, width=int(config.width), style=config.style)
    click.echo(result)


@deploy.command('get')
@click.argument('id', type=int)
@pass_config
def deploy_get(config, id):
    """Get info from deploy"""
    client = Deploy(config.client)
    result = client.get(id)
    header = ('ID', 'Repository ID', 'Environment ID', 'State', 'Version')

    click.echo(result)


@deploy.command('trigger')
@click.argument('id', type=int)
@pass_config
def deploy_get(config, id):
    """Trigger a specific deploy"""
    client = Deploy(config.client)
    result = client.get(id)
    header = ('ID', 'Repository ID', 'Environment ID', 'State', 'Version')

    click.echo(result)
