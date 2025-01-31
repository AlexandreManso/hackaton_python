from .gameobject import GameObject
from .direction import Dir
from .exception import EnnemyEncounter, GameOver
from .Alexandre import Subject, Observer

class Gamer(GameObject, Subject, Observer) :

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
        
        #Apply movement
        self._position += self._dir

        # Notify movement
        for obs in self.observers:
            obs.notify_object_moved(self)

    def notify_collision(self, obj):
        """What to do if a collision is detected."""
        
        #Collided with obstacle
        if obj.is_obstacle:
            self._position -= self._dir
        
        #Collided with ennemy
        if obj.is_enemy:
            raise EnnemyEncounter








class object(GameObject) :
    def __init__(self,t,p,v):
        self.type = t
        self.property = p
        self.value = v
    def potion(object):
        if object.property == "health":
            Gamer.hp = min(5,Gamer.hp+object.value)
    def money(object):
        Gamer.money += object.value
    def draw(object):
        return

class wall(GameObject):
    def __init__(self):
        