# ruff: noqa: D100,S311


import pygame

# First party
from .Alexandre import Board
from .background import Background
from .exception import GameOver, EnnemyEncounter
from .state import State
from .direction import Dir


class Game:
    """The main class of the game."""

    def __init__(self, width: int, height: int,
                 fps: int, tilesize) -> None:
        """Object initialization."""
        self._width = width
        self._height = height
        self._fps = fps
        self._tilesize = tilesize

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
                    self._gamer.move()

            except GameOver:
                self._state=State.GAMEOVER
            
            except EnnemyEncounter:
                self._state=State.PLAY_FIGHT 

            # Display
            pygame.display.update()



        # Terminate pygame
        pygame.quit()

        
