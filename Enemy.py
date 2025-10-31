class Enemy:
    type_of_enemy:str
    health_points:int=100
    attack_damage:int=1

    # default constructor
    # def __init__ (self):#here self means the current object
    #     pass #default constructor does nothing 
    #it is automatically created if no constructor is defined
    #to run some kind of functionality during object creation use the parameter less
    #constructor
    # def __init__(self):
    #     #add some functionality here when an object is created
    #     print("An enemy has been created")

    # parameterized constructor:instead of setting the attributes 
    # after creating the object we want to set it automatically when the object is instantiated
    def __init__(self,type_of_enemy,health_points=500,attack_damage=50):
        self.type_of_enemy=type_of_enemy
        self.health_points=health_points
        self.attack_damage=attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}.Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")
    def attack(self):
        print(f"{self.type_of_enemy} attacks you for {self.attack_damage} damage!")

    def all_info(self):
        print(f"Type of enemy:{self.type_of_enemy}")
        print(f"Health points:{self.health_points}")
        print(f"Attack damage:{self.attack_damage}")