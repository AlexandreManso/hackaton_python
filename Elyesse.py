from .gameobject import GameObject
from .direction import Dir
from .exception import EnemyEncounter, GameOver
from .Alexandre import Subject, Observer


class Gamer(GameObject, Subject, Observer):

    def __init__(self, x, y, sprite, hp, dir, player):
        self._hp = hp
        self._inventory = []
        self._position = (y,x)
        self._sprite = sprite
        self._dir = dir
        self._player = player

    @property
    def dir(self):
        """Set the direction as a property."""
        return self._dir

    @dir.setter
    def dir(self, new_dir: Dir):
        if isinstance(new_dir, Dir):
            self._dir = new_dir
        else:
            msg = f"Wrong object type {type(object)}."
            raise ValueError(msg)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_pos: tuple[int, int]):
        self._position = new_pos

    def add_to_inventory(self, object):
        self.inventory.append(object)

    def move(self):
        """move the player."""

        # Apply movement
        self._position += self._dir

        # Notify movement
        for obs in self.observers:
            obs.notify_object_moved(self)

    def notify_collision(self, obj):
        """What to do if a collision is detected."""

        # Collided with obstacle
        if isinstance(obj, Wall):
            self._position -= self._dir

        # Collided with ennemy
        if isinstance(obj, Gamer) and not obj._player:
            raise EnemyEncounter


class Item(GameObject):
    def __init__(self, x, y, sprite):
        self._position = (y,x)
        self._sprite = sprite


class Wall(GameObject):
    def __init__(self, x,y, length, width, sprite):
        self._position = (y,x)
        self._length = length
        self._width = width
        self._sprite = sprite

    def is_wall(self):
        return True
