#Ici la création de classes
#classe board = tableau avec attribut taille methode add et remove
#classes et sous classes d'objet avec attribut draw

import pygame
from .gameobject import GameObject

class Observer:
    def_init_(self):
        super()._init_()

    def notify_object_moved(self, obj):
        #notify

    def  notify_collision(self, obj):
        #notify

    def notify_out_of_board(self,obj):
        #notify
        
class Subject:

    def __init__(self) -> None:
        """Object initialization."""
        super().__init__()
        self._observers: list[Observer] = []

    @property
    def observers(self) -> list[Observer]:
        """List of observers."""
        return self._observers

    def attach_obs(self, obs: Observer) -> None:
        """Attach an observer."""
        self._observers.append(obs)

    def detach_obs(self, obs: Observer) -> None:
        """Detach an observer."""
        self._observers.remove(obs)


class Board(Subject, Observer):

    def _init_(self, screen: pygame.Surface, nb_lines : int, nb_cols : int):
        super()._init_()
        self._screen = screen
        self._nb_lines = nb_lines
        self._nb_cols = nb_cols
        self._objects: list[GameObject] = []

    def add(self, obj:GameObject):
        if obj not in self._objects:
            self._objects.append(obj)
            obj.attach_obs(self)

    def remove_object(self, obj:GameObject):
        if obj in self._objects:
            self._objects.remove(obj)
            obj.detach_obs(self)

    def draw(self):
        for obj in self._objects:
            obj.draw()
    
    def notify_object_moved(self, obj):
        #DETECT board exit à faire 
        obj.notify_out_of_board()

        #detect collisions
        for o in self.collides(obj):
            obj.notify_collision(o)

        def collides(self, obj):
            for o in self._objects:
                if (obj != o and not(o.is_background()) and (obj in o)):
                    yield o 

