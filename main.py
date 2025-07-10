from enemy import *
from hero import Hero
from weapon import Weapon
from zombie import *
from ogre import *
zombie = Zombie(10, 1)
ogre = Ogre(50, 10)
hero = Hero(100, 10)
weapon = Weapon("Sword", 5)
hero.weapon = weapon
hero.equip_weapon()
def battle(e1: Enemy, e2: Enemy):
    print(e1.talk())
    print(e2.talk())
    while e1.health_points > 0 and e2.health_points > 0:
        print('--------------')
        print(e1.special_attack())
        print(e2.special_attack())
        print(e1.health_points, e1.type_of_enemy)
        print(e2.health_points, e2.type_of_enemy)
        print(e2.attack(e1))
        e1.health_points -= e2.attack_damage
        print(e1.attack(e2))
        e2.health_points -= e1.attack_damage
        print('--------------')
    if e1.health_points > 0:
        print(f"{e1.type_of_enemy} wins!")
    elif e2.health_points > 0:
        print(f"{e2.type_of_enemy} wins!")
    else:
        print("It's a draw!")
def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print('--------------')
        print(hero.attack())
        print(enemy.attack(hero))
        print(hero.health_points, "Hero")
        print(enemy.health_points, enemy.type_of_enemy)
        hero.health_points -= enemy.attack_damage
        enemy.health_points -= hero.attack_damage
        print('--------------')
    if hero.health_points > 0:
        print(f"Hero wins!")
    elif enemy.health_points > 0:
        print(f"{enemy.type_of_enemy} wins!")
    else:
        print("It's a draw!")

        print(enemy.special_attack())
        print(hero.health_points, "Hero")
        print(enemy.health_points, enemy.type_of_enemy)
        print(enemy.attack(hero))
        hero.health_points -= enemy.attack_damage
        print(hero.attack())
        enemy.health_points -= hero.attack_damage
        print('--------------')
    if hero.health_points > 0:
        print(f"Hero wins!")
    elif enemy.health_points > 0:
        print(f"{enemy.type_of_enemy} wins!")
    else:
        print("It's a draw!")

hero_battle(hero,ogre)