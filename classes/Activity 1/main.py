from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player

player_weapon_choices=[
    Weapon("Trusty Dave", random.randint(13,14),"Sword"),
    Weapon("Mace of Doom",15,"Mace"),
    Weapon("Shield of Radience",random.randint(1,20),"Shield"),
    Weapon("Sword of Slashing",15,"Sword")
]

player_choices=[
    Player('Gimli', 'Dwarf', 'Fighter', 6, 180),
    Player('Finlan', 'Elf', 'Wizard', 1, 80),
    Player('Dabin', 'Halfling', 'Monk', 10, 120),
    Player('Dabin', 'Human', 'Cleric', 3, 110),
]
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
Current_enemy = Enemy("Gabe","Gremlin",random.randint(81,139),random.randint(16,17))
print("Player Options:")
i=0
for choice in player_choices:
    i+=1
    print(f"{i}: {choice.info()}")
user_choice = input("Type the number corresponding to the character you want!")
if user_choice == "1":
    player = player_choices[0]
elif user_choice == "2":
    player = player_choices[1]
elif user_choice == "3":
    player = player_choices[2]
elif user_choice == "4":
    player = player_choices[3]
else:
    print("Error")
    exit

for choice in player_weapon_choices:
    i+=1
    print(f"{i}: {choice.info()}")
user_choice = input("Type the number corresponding to the character you want!")
if user_choice == "1":
    weapon = player_weapon_choices[0]
elif user_choice == "2":
    weapon = player_weapon_choices[1]
elif user_choice == "3":
    weapon = player_weapon_choices[2]
elif user_choice == "4":
    weapon = player_weapon_choices[3]
else:
    print("Error")
    exit
# Print the player character details
# TODO: Print the player weapon details
#weapon= random.choice(list(player_weapon_choices))
# TODO: Print the enemy character details
print(player.info(),weapon.info())
print(Current_enemy.info())