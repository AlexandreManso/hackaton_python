# ruff: noqa: D100,S311

# Third Party imports
import pygame
from pathlib import Path
import yaml

# Custom imports
from .Alexandre import Board
from .Elyesse import Gamer, Wall, Item
from .background import Background
from .exception import GameOver, EnnemyEncounter
from .state import State
from .direction import Dir


class Game:
    """The main class of the game."""

    def __init__(self, width: int, height: int,
                 fps: int, tilesize: int, map : dict) -> None:
        """Object initialization."""
        self._width = width
        self._height = height
        self._fps = fps
        self._tilesize = tilesize
        self._map = map

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
        
        # Read the first room
        self._room1 = map["(1,1)"]
        try :
            self._data_room1 = {}
            with self._room1.open("r") as f:
                for dic in yaml.safe_load(f):
                    name = dic.get("name")
                    if name:
                        self._data_room1[name] = dic


        except (FileNotFoundError, yaml.YAMLError) as e:
            print(f"Error {e} while loading file")



        # Load the next accessible rooms
        
        

        # Create the player
        self._gamer = Gamer(x=self._data_room1["player"]["position_x"], 
                            y=self._data_room1["player"]["position_y"], 
                            sprite = self._data_room1["player"]["sprite"] ,
                            hp=self._hp, 
                            dir = self._data_room1["player"]["orientation"],
                            player=True)
        self._board.add_object(self._gamer)
        # Create background
        self._background = Background(height = self._height,
                                          width = self._width)
        self._board.add_object(self._background)

        # Create all other objects
         
        for data in self._data_room1_.items():
            if data['name'].startswith('wall'): 
                # Instantiate Wall
                obj = Wall(data['position_x'],
                           data['position_y'],
                           data['length'],
                           data['width'],
                           data['sprite'])
                self._board.add_object(obj)
            elif data['name'].startswith('enemy'): 
                # Instantiate Enemy
                obj = Gamer(x=data['position_x'], 
                            y=data['position_y'], 
                            hp=data['hp'],
                            sprite=data['sprite'],
                            player=False,
                            dir= None)
                self._board.add_object(obj)
            elif data['name'].startswith('object'):  
                # Instantiate Object
                obj = Item(data['position_x'], data['position_y'], data['sprite'])
                self._board.add_object(obj)

    def _process_play_event(self, event : pygame.event.Event) -> None:
        """Change the direction of the snake if needed."""
        if event.type==pygame.KEYDOWN :

            match event.key:
                case pygame.K_UP:
                    self._gamer.dir = Dir.UP
                case pygame.K_DOWN:
                    self._gamer.dir = Dir.DOWN
                case pygame.K_LEFT:
                    self._gamer.dir = Dir.LEFT
                case pygame.K_RIGHT:
                    self._gamer.dir = Dir.RIGHT

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
            
            except EnemyEncounter:
                self._state=State.PLAY_FIGHT 

            # Display
            pygame.display.update()



        # Terminate pygame
        pygame.quit()

        
