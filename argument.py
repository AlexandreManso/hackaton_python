import argparse
from pathlib import Path



#Global constants
DEFAULT_MAPPING = {"(1,1)" : Path("mappings/mapping1.yml")}


def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    parser = argparse.ArgumentParser(
        description = "Rogue-like game.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--MAPPING1", "-MP1"
                        help= ".yaml file for the screens.",
                        default= DEFAULT_MAPPING)
    
    
    args = parser.parse_args()
    
    for 
