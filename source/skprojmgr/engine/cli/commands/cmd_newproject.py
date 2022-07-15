from skprojmgr.engine.cli.shell import pass_environment
import click


@click.command("newproject", short_help="Create new project, make source root and additional dirs")
# @click.option()
@pass_environment
def newproject(ctx):
    """
    Command `newproject` – Create new project, make source root and additional dirs | cmd_newproject.py
    """
