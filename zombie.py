from enemy import *

class Zombie(Enemy):
    def __init__(self, health, damage):
        super().__init__("Zombie", health, damage)

    def attack(self, target):
      return "Zombie attacks with a bite!" if isinstance(target, Zombie) else "Target is not a Zombie!"

    def talk(self):
        return "Zombie groans menacingly!"

    def spread_infection(self, target):
        if isinstance(target, Zombie):
            print(f"{self.type_of_enemy} spreads infection to {target.type_of_enemy}!")
        else:
            print("Target is not a Zombie!")