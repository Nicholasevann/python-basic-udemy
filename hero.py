from weapon import Weapon
class Hero:
    def __init__(self,health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon:Weapon = None
    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.is_weapon_equipped = True
            self.attack_damage += self.weapon.bonus_damage
    def attack(self):
        return f"Hero attacks with {self.attack_damage} damage."