import argparse
from pathlib import Path


# Global constants
DEFAULT_MAPPING = Path("mapping.yml")
DEFAULT_


def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    parser = argparse.ArgumentParser(
        description="Rogue-like game.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args = parser.parse_args()
    return args
