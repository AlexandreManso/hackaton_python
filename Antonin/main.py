# Standard
import sys

# First party
from .arguments import read_args
from .exceptions import GameError
from .game import Game


def main() -> None: # noqa: D103

    try:
        # Read command line arguments
        args = read_args()

        # Start game
        Game(width = args.width, height = args.height,
              fps = args.fps,
            ).start()

    except GameError as e:
        print(f"Error: {e}") # noqa: T201
        sys.exit(1)