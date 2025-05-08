class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race (e.g., human, elf, etc.)
        self.cls = cls        # Store the player's class (e.g., warrior, mage, etc.)
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

class Weapon:
    def __init__(self,name,damage,catagory):
        self.name = name
        self.damage = damage
        self.catagory = catagory
    # TODO: create the method to intialise Weapon object attributes (same as above)
    # The Weapon should have self, name, category and damage (can shorten if needed)
# TODO: Create an 'Enemy' class.
class Enemy:
    def __init__(self,name,race,health,damage):
        self.name = name
        self.damage = damage
        self.race = race
        self.health = health
    # TODO: Create a method to initialise Enemy object attributes
    # Each enemy should have a name, race, damage and health