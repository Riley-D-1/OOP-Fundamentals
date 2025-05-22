from weapons import *

class Sword(Weapon):
    def __init__(self,name,catagory,damage,damage_catagory):
        super().__init__(self,name,catagory,damage)
        self.damage_catagory = damage_catagory
    def get_stats(self,damage_catagory):
        super().get_stats(self)
        self.damage_catagory = damage_catagory









