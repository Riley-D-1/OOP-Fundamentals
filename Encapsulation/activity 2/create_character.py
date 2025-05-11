class character:
    def __init__(self,name,cls,lvl):
        self.name = name
        self.cls =  cls
        self.lvl = lvl 
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string.")
    def set_lvl(self, lvl):
        if isinstance(lvl, int):
            self._name = lvl
        else:
            raise ValueError("LvL must be a int.")
    def info(self):
        return self.name, self.cls, self.lvl