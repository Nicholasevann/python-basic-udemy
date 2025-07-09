from enemy import *

class Ogre(Enemy):
    def __init__(self, health, damage):
        super().__init__("Ogre", health, damage)

    def attack(self, target):
       return "Ogre swings a massive club!" if isinstance(target, Ogre) else "Target is not an Ogre!"

    def talk(self):
        return "Ogre grunts and bellows!"
    def stomp_ground(self):
        return f"{self.name} stomps the ground, causing a minor earthquake!"