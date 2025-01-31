import argparse
from pathlib import Path



#Global constants
DEFAULT_MAPPING = {"(1,1)" : Path("mappings/mapping1.yml")}
DEFAULT_HEIGHT = 800
DEFAULT_WIDTH = 1200
DEFAULT_TILESIZE = 40



def read_args() -> argparse.Namespace:
    """Read command line arguments."""

    parser = argparse.ArgumentParser(
        description = "Rogue-like game.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--MAPPING", "-MP",
                        help= "Dictionnary with screens.",
                        default= DEFAULT_MAPPING)
    parser.add_argument("--HEIGHT", "-ht",
                        help = "Height of the screen.",
                        default = DEFAULT_HEIGHT,
                        type = int)
    parser.add_argument("--WIDTH", "-wd",
                        help = "Width of the screen.",
                        default = DEFAULT_WIDTH,
                        type = int)
    parser.add_argument("--TILESIZE", "-ts",
                        help = "Size for a tile.",
                        default = DEFAULT_TILESIZE,
                        type= int)
    args = parser.parse_args()
    return args

    
