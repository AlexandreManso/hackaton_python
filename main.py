# Standard
import sys

# Custom imports
from .argument import read_args
from .exception import GameError
from .game import Game


def main() -> None:  # noqa: D103

    try:
        # Read command line arguments
        args = read_args()

        # Start game
        Game(
            width=args.WIDTH,
            height=args.HEIGHT,
            fps=args.FRAMERATE,
            map=args.MAPPING,
            hp = args.HEALTH,
            tilesize = args.TILESIZE,
        ).start()

    except GameError as e:
        print(f"Error: {e}")  # noqa: T201
        sys.exit(1)
