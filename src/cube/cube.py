import argparse
from cli import Shuffle


def init_cli():
    parser = argparse.ArgumentParser(description="cli tool for rubix cube")
    subparser = parser.add_subparsers(dest="subcmd", help="cmd help")

    Shuffle(subparser)



    return parser



if __name__ == "__main__":
    parser = init_cli()

    try:
        args = parser.parse_args()
        args.func(args)
    except Exception as e:
        print(e)
        parser.print_help()
