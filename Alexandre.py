#Ici la création de classes
#classe board = tableau avec attribut taille methode add et remove
#classes et sous classes d'objet avec attribut draw

import pygame


class Board:
    def_init_(self, screen: pygame.Surface, nb_lines : int, nb_cols : int):
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