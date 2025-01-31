from enum import Enum


class State(Enum):
    """Define the states of the game."""

    MENU = 0
    PLAY_ROAM = 1
    PLAY_FIGHT = -1
    GAMEOVER = 2
    QUIT = 3
