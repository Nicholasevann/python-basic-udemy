from enemy import *
import random
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
    def special_attack(self):
        did_special_attack = random.random() < 0.5
        if did_special_attack:
            self.health_points += 5
            return f"{self.type_of_enemy} performs a special attack, smashing the ground and sending shockwaves!"
        else:
            return f"{self.type_of_enemy} tries to perform a special attack but fails!"