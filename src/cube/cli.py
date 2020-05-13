from sub_cmd import Subcommand


class Shuffle(Subcommand):


    def __init__(self, subparser):
        super().__init__(name="shuffle", aliases=[], help="shows a string of shuffle instruction", subparser=subparser)
    # end



    def execute(self, *args):
        print("2R L F 2R")
    # end

# end
