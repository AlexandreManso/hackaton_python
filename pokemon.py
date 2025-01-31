import random

class Pokemon:
    def __init__(self, name, level, hp, attack, defense, moves):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def choose_move(self):
        print(f"{self.name}'s moves: {', '.join(self.moves)}")
        move = input("Choose a move: ")
        while move not in self.moves:
            print("Invalid move! Please choose again.")
            move = input("Choose a move: ")
        return move

    def attack_opponent(self, move, opponent):
        damage = random.randint(5, 10) + self.attack - opponent.defense
        if damage < 0:
            damage = 0
        print(f"{self.name} uses {move} and deals {damage} damage!")
        opponent.take_damage(damage)


def battle(pokemon1, pokemon2):
    print(f"A wild {pokemon2.name} appeared!\n")
    while pokemon1.is_alive() and pokemon2.is_alive():
        print(f"\n{pokemon1.name} HP: {pokemon1.hp}/{pokemon1.max_hp} | {pokemon2.name} HP: {pokemon2.hp}/{pokemon2.max_hp}")
        
        move1 = pokemon1.choose_move()
        pokemon1.attack_opponent(move1, pokemon2)
        
        if pokemon2.is_alive():
            move2 = pokemon2.choose_move()
            pokemon2.attack_opponent(move2, pokemon1)
        else:
            print(f"{pokemon2.name} has fainted!")
            break

        if not pokemon1.is_alive():
            print(f"{pokemon1.name} has fainted!")
            break

    print("Battle Over!")

# Create some Pokémon
bulbizare = Pokemon("bulbizare", level=5, hp=40, attack=10, defense=5, moves=["charge", "cri"])
salameche = Pokemon("salameche", level=5, hp=39, attack=12, defense=4, moves=["flamèche", "cri"])

# Start the battle
battle(bulbizare, salameche)
