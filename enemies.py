

class Enemy():
    def __init__(self, hp):
        self.hp = hp
        pass
    
    def is_alive(self):
        return self.hp > 0


class Armour(Enemy):
    def __init__(self):
        pass

class AntiAir(Enemy):
    def __init__(self):
        pass

class Dissmounts(Enemy):
    def __init__(self):
        pass

class MBT(Armour):
    def __init__(self):
        pass

class Recce(Armour):
    def __init__(self):
        pass

