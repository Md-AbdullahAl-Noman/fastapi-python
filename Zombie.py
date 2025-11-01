from Enemy import *

class Zombie(Enemy):
    def __init__(self,health_points,attack_damage):
        super().__init__(type_of_enemy="Zombie"
                         ,health_points=health_points
                         ,attack_damage=attack_damage)


    #method overriding
    def talk(self):
        print(f"hey this is a zombie!Brains...Brains...my talkkkkk")