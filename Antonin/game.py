# ruff: noqa: D100,S311

# Third party
import importlib.resources
import sys
from pathlib import Path

import pygame

# First party
from .board import Board
from .background import Background
from .dir import Dir
from .exceptions import GameOver
from .state import State


class Game:
    """The main class of the game."""

    def __init__(self, width: int, height: int,
                 fps: int) -> None:
        """Object initialization."""
        self._width = width
        self._height = height
        self._fps = fps

    def _init(self) -> None:
        """Initialize the game."""
        # Create a display screen
        screen_size = (self._width,
                       self._height)
        self._screen = pygame.display.set_mode(screen_size)

        # Create the clock
        self._clock = pygame.time.Clock()

        # Create the main board
        self._board = Board(screen = self._screen,
                            nb_lines = self._height,
                            nb_cols = self._width)

        # Create background
        self._background = Background(height = self._height,
                                          width = self._width)
        self._board.add_object(self._background)

    def _process_play_event(self, event : pygame.event.Event) -> None:
        """Change the direction of the snake if needed."""
        if event.type==pygame.KEYDOWN :
            match event.key:
                case pygame.K_UP:
                    self._snake.dir = Dir.UP
                case pygame.K_DOWN:
                    self._snake.dir = Dir.DOWN
                case pygame.K_LEFT:
                    self._snake.dir = Dir.LEFT
                case pygame.K_RIGHT:
                    self._snake.dir = Dir.RIGHT

    def _process_events(self) -> None:
        """Process pygame events."""
        # Loop on all events
        for event in pygame.event.get():

            match self._state :
                case State.MENU :
                    pass
                case State.PLAY_ROAM :
                    self._process_play_event(event)
                case State.PLAY_FIGHT :
                    pass
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                self._state = State.QUIT

            # Key press
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                self._state= State.PLAY

                # Quit
                match event.key:
                    case pygame.K_q:
                        self._state = State.QUIT

    def start(self) -> None:
        """Start the game."""
        # Initialize pygame
        pygame.init()

        # Initialize game
        self._init()

        # Start pygame loop
        self._state = State.MENU
        while self._state != State.QUIT:

            # Wait 1/FPS second
            self._clock.tick(self._fps)

            # Listen for events
            self._process_events()

            # Update objects
            try :
                if self._state==State.PLAY_ROAM :
                    self._.move()

            except GameOver:
                self._state=State.GAMEOVER
                countdown=self._fps



            # Draw
            self._board.draw()
            match self._state :
                case State.GAMEOVER :

                    #Draw gameover for a given timespan
                    self._drawgameover()
                    countdown-=1
                    if countdown==0 :

                        #Replace Snake to a correct position
                        score=self._snake.score
                        self._reset_snake()

                        #Manage score
                        if self._scores.is_highscore(score) is True :
                            self._new_high_score=Score(name="", score=score)
                            self._scores.add_score(self._new_high_score)
                            self._state= State.INPUT_NAME
                        else :
                            self._state=State.SCORES
                case State.SCORES | State.INPUT_NAME:
                    self._draw_scores()

            # Display
            pygame.display.update()



        # Terminate pygame
        pygame.quit()

        
