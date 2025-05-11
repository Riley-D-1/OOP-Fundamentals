from create_character import *
dave=character("Dave","Orc",21)
daniel=character("Daniel","Human",21)
dave.set_name("Dave The great")
dave.set_lvl(23)
daniel.set_lvl(25)
daniel.set_name("Daniel the boring")
print(daniel.info(),dave.info())
