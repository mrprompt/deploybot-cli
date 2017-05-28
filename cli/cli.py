import click
from .user import user
from .server import server
from .environment import environment
from .repository import repository
from .deploy import deploy


@click.group()
def cli():
    pass

cli.add_command(user)
cli.add_command(server)
cli.add_command(environment)
cli.add_command(repository)
cli.add_command(deploy)
