from Enemy import *
enemy1=Enemy(type_of_enemy="Zombie")

enemy1.health_points=120

enemy1.talk()#here abstraction is used as we are calling a method 
#without knowing the inner working of it
print(enemy1.health_points)
# print(enemy1.__type_of_enemy)#cant access as it is private attribute and thus we achieved 
#encapsulation here as we restricted direct access to the attribute from outside of the class
#because encapsulation means restricting direct access to some of the object's components from outside world
#so we can offer controlled access by using setter and getter methods if needed and those are public methods
type=enemy1.get_type_of_enemy()
print(f"The type of enemy by encapsulation is {type}")
enemy2= Enemy("Vampire")
enemy2.all_info()