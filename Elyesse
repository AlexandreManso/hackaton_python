class gamer(GameObject) :
    def __init__(self,x,y):
        self.hp = 5
        self.inventory = []
        self.position = (x,y)
        self.money = 0
    def add_to_inventory(self,object):
        self.inventory.append(object)

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
        