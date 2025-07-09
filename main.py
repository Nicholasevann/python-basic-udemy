from enemy import *
from zombie import *
from ogre import *
zombie = Zombie(10, 1)
ogre = Ogre(50, 10)

def battle(e: Enemy):
    talk_result = e.talk()
    attack_result = e.attack(e)
    return f"{talk_result}\n{attack_result}"

print(battle(zombie))
print(battle(ogre))