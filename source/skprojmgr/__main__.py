import clickfrom skprojmgr.engine.cli import shellCLI_SHELL = shell.CLIShell(help="This tool's subcommands are loaded")# @click.group()# def skprojadmin():#     pass## @click.command()# def cli(cls=CLI_SHELL):#     pass@click.group()def cli():    pass@cli.group(cls=shell.group_from_folder())def cli_grup():if __name__ == "__main__":    cli()