from .gameobject import GameObject
from .direction import Dir

class gamer(GameObject, Subject, Observer) :

    def __init__(self,x,y, hp, money, speed, dir):
        self._hp = hp
        self._inventory = []
        self._position = (x,y)
        self._money = money
        self._speed = speed
        self._dir = dir

    @property
    def dir(self):
        """Set the direction as a property."""
        return self._dir
    
    @dir.setter
    def dir(self, new_dir : Dir):
        if isinstance(new_dir, Dir):
            self._dir = new_dir
        else :
            msg = f"Wrong object type {type(object)}."
            raise ValueError(msg)
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, new_pos : tuple[int, int]):
        self._position = new_pos

    
    def add_to_inventory(self,object):
        self.inventory.append(object)
    
    def move(self):
        """move the player."""
        self._position += self._dir






class object(GameObject) :
    def __init__(self,t,p,v):
        self.type = t
        self.property = p
        self.value = v
    def potion(object):
        if object.property == "health":
            gamer.hp = min(5,gamer.hp+object.value)
    def money(object):
        gamer.money += object.value
    def draw(object):
        return

class wall(GameObject):
    def __init__(self):
        