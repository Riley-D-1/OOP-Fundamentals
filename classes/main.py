from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player

player_weapon_choices={
    Weapon("Trusty Dave", random.randint(13,14),"Sword"),
    Weapon("Mace of Doom",15,"Mace"),
    Weapon("Shield of Radience",random.randint(1,20),"Shield"),
    Weapon("Sword of Slashing",15,"Sword")
}

player_choices={
    Player('Gimli', 'Dwarf', 'Fighter', 6, 180),
    Player('Finlan', 'Elf', 'Wizard', 1, 80),
    Player('Dabin', 'Halfling', 'Monk', 10, 120),
    Player('Dabin', 'Human', 'Cleric', 3, 110),
}
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
Current_enemy = Enemy("Gabe","Gremlin",random.randint(81,139),random.randint(16,17))

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
print(f"Weapon Name: {player_weapon.name}")
print(f"Weapon Class: {player_weapon.catagory}")
print(f"Weapon Damage: {player_weapon.damage}")
# TODO: Print the enemy character details
print(f"Enemy Name: {Current_enemy.name}")
print(f"Enemy Race: {Current_enemy.race}")
print(f"Enemy Attack: {Current_enemy.damage}")
print(f"Enemy Health: {Current_enemy.health}")