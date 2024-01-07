import argparse

parser = argparse.ArgumentParser(description="A command line dice roller")

parser.add_argument("dice",  help="A representation of the dice you want to roll")

parser.add_argument(
    "-r",
    "--repeat",
    metavar = "number",
    default = 1,
    type = int,
    help = "How many times to roll the specifed set of dice"
)

parser.add_argument(
    "-l",
    "--log",
    metavar="path",
    default="roll_log.txt",
    type=str,
    help="A file to use to log the result of the rolls"
)


def parse_roll(args):
    try:
        quantity, die_size = [int(arg) for arg in args.dice.split("d")]
    except ValueError:
        raise ValueError("Invalid dice specification. Rolls must be in the format of 2d6") from None

    return quantity, die_size


args = parser.parse_args()