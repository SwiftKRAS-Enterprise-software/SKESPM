import click
import os


def group_from_folder(group_folder_name):
    folder = os.path.join(os.path.dirname(__file__), group_folder_name)

    class FolderCommands(click.MultiCommand):

        def list_commands(self, ctx):
            return sorted(
                f[:-3] for f in os.listdir(folder) if f.endswith('.py'))

        def get_command(self, ctx, name):
            namespace = {}
            command_file = os.path.join(folder, name + '.py')
            with open(command_file) as f:
                code = compile(f.read(), command_file, 'exec')
                eval(code, namespace, namespace)
            return namespace[name.replace('-', '_').lower()]

    return FolderCommands
