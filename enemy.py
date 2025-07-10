class Enemy:
    def __init__(self,type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    def talk(self):
        return(f'I am a {self.type_of_enemy} enemy with {self.health_points} health points and {self.attack_damage} attack damage.')
    def walk_forward(self):
        return(f'The {self.type_of_enemy} enemy is walking forward.')
    def attack(self):
        return(f'The {self.type_of_enemy} enemy attacks with {self.attack_damage} damage.')
    def special_attack(self):
        return(f'The {self.type_of_enemy} enemy performs a special attack!')