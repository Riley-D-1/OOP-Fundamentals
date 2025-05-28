class Weapon():
    def __init__(self,name,catagory,damage):
        self.name = name
        self.catagory = catagory
        self.damage = damage
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Damage: {self.damage}")
        
class Sword(Weapon):
    def __init__(self,name,catagory,damage,damage_catagory):
        super().__init__(name,catagory,damage)
        self.damage_catagory = damage_catagory
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Damage: {self.damage}")
        print(f"Damage activity: {self.damage_catagory}")
        print(f"Crit damage: {self.damage * 3}")

class Bow(Weapon):
    def __init__(self,name,catagory,damage,damage_catagory):
        super().__init__(name, catagory, damage)
        self.damage_catagory = damage_catagory
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Damage: {self.damage}")
        print(f"Damage activity: {self.damage_catagory}")
        print(f"Crit damage: {self.damage * 3}")

class Longbow(Bow):
    def __init__(self,name,catagory,damage,damage_catagory):
        super().__init__(name,catagory,damage,damage_catagory)    
        self.Bow_range = 150
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Damage: {self.damage}")
        print(f"Damage activity: {self.damage_catagory}")
        print(f"Crit damage: {self.damage * 3}")
        print(f"Bow range in ft: {self.Bow_range}")

class Shortbow(Bow):
    def __init__(self,name,catagory,damage,damage_catagory):
        super().__init__(name,catagory,damage,damage_catagory)    
        self.Bow_range = 80
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Damage: {self.damage}")
        print(f"Damage activity: {self.damage_catagory}")
        print(f"Crit damage: {self.damage * 3}")
        print(f"Bow range in ft: {self.Bow_range}")
