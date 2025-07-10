from enemy import *
import random
class Ogre(Enemy):
    def __init__(self, health, damage):
        super().__init__("Ogre", health, damage)

    def attack(self, target):
       return "Ogre swings a massive club!" if isinstance(target, Ogre) else "Target is not an Ogre!"

    def talk(self):
        return "Ogre grunts and bellows!"
    def stomp_ground(self):
        return f"{self.name} stomps the ground, causing a minor earthquake!"
    def special_attack(self):
        did_special_attack = random.random() < 0.2
        if did_special_attack:
            self.health_points += 4
            return f"{self.type_of_enemy} performs a special attack, smashing the ground and sending shockwaves!"
        else:
            return f"{self.type_of_enemy} tries to perform a special attack but fails!"