from deploybot.deploy import Deploy
from .config import Config
from . import response
from io import StringIO
import click
import tableprint

output = StringIO()
pass_config = click.make_pass_decorator(Config, ensure=True)
header = ('ID', 'Repository ID', 'Environment ID', 'State', 'Version')


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
    data = response('deploy', 'list', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())


@deploy.command('get')
@click.argument('id', type=int)
@pass_config
def deploy_get(config, id):
    """Get info from deploy"""
    client = Deploy(config.client)
    result = client.get(id)
    data = response('deploy', 'get', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())


@deploy.command('trigger')
@click.argument('id', type=int)
@pass_config
def deploy_get(config, id):
    """Trigger a specific deploy"""
    client = Deploy(config.client)
    result = client.get(id)
    data = response('deploy', 'trigger', result)

    tableprint.table(data, headers=header, width=int(config.width), style=config.style, out=output)
    click.echo(output.getvalue())
