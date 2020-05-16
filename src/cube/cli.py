import random
import time
from sub_cmd import Subcommand



class Shuffle(Subcommand):


    def __init__(self, subparser):
        super().__init__(name="shuffle", aliases=[], help="shows a string of shuffle instruction", subparser=subparser)
        self.alphabth = ["F","2F","F'", "R","2R","R'",
                         "U","2U","U'", "L","2L","L'",
                         "B","2B","B'", "D","2D","D'",
                        ]
        self.side = ['yellow', 'white', 'blue', 'green', 'red', 'orange']
    # end

    def setup(self, subparser):
        super().setup(subparser)
        self.cmd_parser.add_argument(
                        '-t', '--times', dest="times", metavar="Times", type=int, default=12,
                        help="how many shuffle instructions should be shown, default: 12"
        )
        self.cmd_parser.add_argument(
                        '-s', '-seed', dest="seed", metavar="Seed", type=int, default=time.clock,
                        help="specify the seed for the random numbers, default: time.clock()")

    def execute(self, args):
        random.seed(args.seed)
        result = []
        while len(result) <= args.times:
            letter = self._get_random_letter()

            if len(result) >= 1:
                if  not result[-1] == letter:
                    result.append(letter)
            else:
                result.append(letter)
        # end
        start_side = self.side[random.randint(1, len(self.side)-1)]
        print("\n", start_side, sep="")
        print(" ".join(result))
    # end



    def _get_random_letter(self) -> str:
        return self.alphabth[random.randint(1, len(self.alphabth)-1)]
    # end
# end
