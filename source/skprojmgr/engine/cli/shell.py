import clickimport osimport sysclass Environment:    def __init__(self):        self.verbose = False        self.home = os.getcwd()    def log(self, msg, *args):        """Logs a message to stderr."""        if args:            msg %= args        click.echo(msg, file=sys.stderr)    def vlog(self, msg, *args):        """Logs a message to stderr only if verbose is enabled."""        if self.verbose:            self.log(msg, *args)pass_environment = click.make_pass_decorator(Environment, ensure=True)cmd_folder = os.path.abspath(os.path.join(    os.path.dirname(__file__),    'commands'))def group_from_folder():    class FolderCommands(click.MultiCommand):        def list_commands(self, ctx):            return sorted(                f[:-3] for f in os.listdir(cmd_folder) if f.endswith('.py'))        def get_command(self, ctx, name):            namespace = {}            command_file = os.path.join(cmd_folder, "cmd_" + name + ".py")            with open(command_file) as f:                code = compile(f.read(), command_file, 'exec')                eval(code, namespace, namespace)            return namespace[name.replace('-', '_').lower()]    return FolderCommandsclass CLIShell(click.MultiCommand):    def list_commands(self, ctx):        rv = []        for filename in os.listdir(cmd_folder):            if filename.endswith(".py") and filename.startswith("cmd_"):                rv.append(filename[4:-3])            # if filename.endswith('.py') and filename != '__init__.py':            #     rv.append(filename[:-3])        rv.sort()        return rv    def get_command(self, ctx, name):        # try:        #     mod = __import__(f"complex.commands.cmd_{name}", None, None, ["cli"])        # except ImportError:        #     return        # return mod.cli        ns = {}        fn = os.path.join(cmd_folder, "cmd_" + name + ".py")        with open(fn) as f:            code = compile(f.read(), fn, 'exec')            eval(code, ns, ns)        return ns['cli']@click.group(cls=group_from_folder())def group():    pass