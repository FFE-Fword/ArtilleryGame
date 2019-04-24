""" CLASSES work with basic functionality. Contains all enemy classes. They all have base variables of hp (health), armour and a base description. When enemies take damage, their armour will deplete until 0, then hp will deplete."""


class Enemy():  # All enemies a derived from this class

    base_hp = 100
    base_armour = 100
    description = ("An enemy of Canada that must not be allowed"
    " to live!!!")

    def __str__(self):
        return "{}".format(self.description)

    # Checks if enemy health is above 0

    def is_alive(self):
        return self.base_hp > 0

    # Takes in amount(amt) as an int and adds to    self.base_armour

    def add_armour(self, amt):
        self.base_armour += amt

    # Function that detucts taken damage from armour

    def lose_armour(self, damage):
        self.base_armour -= damage
        return self.base_armour


# Armour, AntiAir and Dissmounts direct child of Enemy()

class Armour(Enemy):
       def __init__(self):
            super().__init__() 
            self.base_hp *= 1.25
            self.base_armour *= 1
            self.description = ("The enemy apears to be hatches down in some" "sort of armoured vehicle")


""" TODO: add functions to dissmounts to add more armour if they have some
    sort of cover ie. OHP, Dug-in. Possibliy cover can be chosen from a
    list of covers"""


class Dissmounts(Enemy):  # No armour unless under cover.
    def __init__(self, cover=None):
        super().__init__()
        self.cover = cover
        self.base_hp *= 0.5
        self.base_armour = 0
        self.description = ("Enemy soldiers. Basic grunts. Very vulnerable"
            " in the open but harder to kill once dug-in.")


""" These 3 are direct from Armour(). Armour is being multiplied by a set
    value. Might be a better way of doing this."""


class AntiAir(Armour):
    def __init__(self):
        super().__init__()
        self.base_armour *= 0.5
        self.description = ("It's a enemy air defence vehicle! This should "
            "be a top priority kill.")


class MBT(Armour):
    def __init__(self):
        super().__init__()
        self.base_armour *= 1.25
        self.description = ("Enemy MBT out of concealment! Prime target for "
            "the Guns!")


class Recce(Armour):
    def __init__(self):
        super().__init__()
        self.base_armour *= 0.75
        self.description = ("Light and fast, recce vehicles aren't "
                            "made to take a hit.")


tsevtwo = MBT()
zsu = AntiAir()
print(zsu.base_armour)
print(tsevtwo.base_armour)
print(tsevtwo.base_hp)
print(zsu)
