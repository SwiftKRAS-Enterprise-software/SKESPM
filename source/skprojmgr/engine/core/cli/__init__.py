import click
import os
import sys

from skprojmgr.engine.core.cli.commands import group_from_folder


class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'commands'
))


@click.group()
def cli():
    """CLI Initialization"""


@cli.group(cls=group_from_folder('project_admin'))
def project_admin():
    """Group with project cmds"""


@cli.group(cls=group_from_folder('framework_admin'))
def framework_admin():
    """Group with framework cmds"""


@cli.group(cls=group_from_folder('utilities'))
def utilities():
    """Group with utils cmds"""

