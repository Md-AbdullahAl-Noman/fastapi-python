from Enemy import *
enemy1=Enemy(type_of_enemy="Zombie")

enemy1.health_points=120

enemy1.talk()#here abstraction is used as we are calling a method 
#without knowing the inner working of it
print(enemy1.health_points)

enemy2= Enemy(type_of_enemy="Vampire")
enemy2.all_info()