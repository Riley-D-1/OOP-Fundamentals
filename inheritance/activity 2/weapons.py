class Weapon():
    def __init__(self,name,catagory,damage):
        self.name = name
        self.catagory = catagory
        self.damage = damage
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Damage: {self.damage}")
        
