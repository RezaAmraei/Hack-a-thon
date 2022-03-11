# Use the starter code to make a RPG battle game between ninjas and pirates.
# Customize the attack methods on both the Ninja and Pirate class.
# Have an instance of a ninja and pirate battle it out until one's health is depleted.
# Ninja Bonus: Use Inheritance, Class Methods, and Static Methods within your code.

import random

class Weapon:
    def __init__(self, WeaponName = "Hands", WeaponStrength = 20):
        self.WeaponName = WeaponName
        self.WeaponStrength = WeaponStrength


class NinjaWeapon(Weapon):
    def __init__(self, WeaponName, WeaponStrength):
        super().__init__(WeaponName, WeaponStrength)
        

    def ninjaWeaponAttack(self):
        print(self.WeaponName)

class PirateWeapon(Weapon):
    def __init__(self, WeaponName, WeaponStrength):
        super().__init__(WeaponName, WeaponStrength)
        
    
    # def pirateWeaponAttack(self):
    #     pass

class Ninja():
    def __init__( self , name):
        self.name = name
        self.strength = 10
        self.speed = 10
        self.health = 100
        
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        

    def attack( self , pirate ):
        print(f"Hiyaaaaaaaa {self.name} Im attacking you {pirate.name} ")
        pirate.health -= random.randint(5, self.strength)
        return self
    
    def buff(self):
        print(f"Eats a slice of pizza")
        self.health += 25

class Pirate:
    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 5
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        print(f"Arrrrrrrr I {self.name} Im attacking you {ninja.name} ")
        ninja.health -= random.randint(5, self.strength)
        return self

    def buff(self):
        print(f"Unscrews hook hand and opens bottle")
        self.health += 20

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

def runGame(pirate, ninja):
    count = 1
    buffCountPirate = 0
    buffCountNinja = 0

    while pirate.health > 0 and ninja.health > 0:
        print(f'--------------Turn {count} ------------------------')
        if pirate.speed >= ninja.speed:
            # Pirate Attacks First
            if pirate.health < 10 and buffCountPirate == 0:
                pirate.buff()
                ninja.attack(pirate)
                buffCountPirate += 1
            elif ninja.health < 15 and buffCountNinja == 0:
                ninja.buff()
                pirate.attack(ninja)
                buffCountNinja += 1
            else:
                pirate.attack(ninja)
                ninja.attack(pirate)
        else:
            # Ninja Attacks First
            if pirate.health < 10 and buffCountPirate == 0:
                ninja.attack(pirate)
                pirate.buff()
                buffCountPirate += 1
           
            elif ninja.health < 15 and buffCountNinja == 0:
                ninja.buff()
                pirate.attack(ninja)
                buffCountNinja += 1
            else:
                ninja.attack(pirate)
                pirate.attack(ninja)
        print("Pirates Health - ",pirate.health)
        print("Ninjas Health - ",ninja.health)
        count += 1
    if pirate.health <= 0:
        print(ninja.name , " Won")
    else:
        print(pirate.name , " Won")
runGame(jack_sparrow, michelangelo)
# print(michelangelo.show_stats())

