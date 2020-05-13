from abc import ABC, abstractmethod

def make_command(func):
    """
    decorator to setup basic subcommand infos

    will set the command, name, aliases and help text
    """
    def wrapper(self, subparser):
        self.cmd_parser = subparser.add_parser(self.cmd_name, aliases=self.cmd_aliases, help=self.cmd_help)
        func(self, subparser)

    # end
    return wrapper
# end

class Subcommand(ABC):
    """ Class with provide basic Features to build a Subcommands """

    @abstractmethod
    def __init__(self, **kwargs):
        self.cmd_name = kwargs["name"]
        self.cmd_aliases = kwargs["aliases"]
        self.cmd_help = kwargs["help"]
        self.cmd_parser = None
        self.setup(kwargs["subparser"])
        self.alphabth = ["F", "R", "U", "L", "B", "D"]

    # @abstractmethod
    @make_command
    def setup(self, subparser):
        """
        setup the sub command parser

        sets the function with will exetuted by the argparse framework
        """
        self.cmd_parser.set_defaults(func=self.execute)

    @abstractmethod
    def execute(self, *args):
        pass
    # end


    def get_aliases(self):
        """ generator for all names of the command eihter name or aliases """
        yield self.cmd_name
        yield from self.cmd_aliases
    # end
# end
