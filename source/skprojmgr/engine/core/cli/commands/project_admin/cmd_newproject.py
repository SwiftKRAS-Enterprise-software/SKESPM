import click
from pathlib import Path

from skprojmgr.engine.bin import home_dir
from skprojmgr.utility.filesystem import create_dir

DEFAULT_LOCATION_FOR_NEW_PROJECTS = Path(home_dir, "PROJECTS")

# project_structures = {
#     "all": (
#         (".skes/", ".skesproject.conf.tmpl"
#          "docs/", ".github/", "tests/")
#     ),
#     "simple": (
#         ("source/", ("core/", "util/", "misc/"))
#     ),
#     "python-pkg": (
#         ("source/",
#          ("$NAME$/",
#           ("core/", "conf/", "handlers/", "utils/",)
#           )
#
#     )
# }


@click.command(name="newproject", short_help="Create and registr in framework db new project")
@click.option(
    "--name", "-N",
    prompt="Project name (using in DB, Framework CLI and Filesystem)",
    default="NewSKESProject",
)
@click.option(
    "--src", "--dist", "--path", "--location", "-D",
    type=click.Path,
    default=None,
    required=False
)
@click.option(
    "--tmpl", "-T",
    type=click.Choice([
        "simple",
        "python-pkg",
        "desktop-gui", "cli",
        "mobile", "mobile-apple",
        "BLANKPROJECT"
    ]),
    default="simple",
    show_default=True
)
def newproject(name, location, project_type):
    """
    Command `newproject` – Create and registr in framework db new project
    location :: source/skprojmgr/engine/core/cli/commands/project_admin/newproject.py
    """
    _onCalled = None
    _onCalled.echo_msg = "Start creating new project"
    if bool(len(_onCalled.echo_msg)):
        click.echo(_onCalled.echo_msg)

    project = object
    project.name = name

    project.dir = Path(
        DEFAULT_LOCATION_FOR_NEW_PROJECTS, project.name

    )
    create_dir(project.dir)
