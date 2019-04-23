

""" CLASSES DO NOT WORK YET!!!!!Contains all enemy classes. They all have base      variables of hp (health), armour and a base description. When enemies take      damage, their armour will deplete until 0, then hp will deplete."""


class Enemy():  # All enemies a derived from this class

    def __init__(self):
        self.hp = 100
        self.armour = 100
        self.description = "An enemy of Canada that must not be allowed ",\
            "to live!!"

    # Checks if enemy health is above 0

    def is_alive(self):
        return self.hp > 0

    # Takes in amount(amt) as an int and adds to self.armour

    def add_armour(self, amt):
        self.armour += amt

    # Function that detucts taken damage from armour

    def lose_armour(self, damage):
        self.armour -= damage
        return self.armour


# Armour, AntiAir and Dissmounts direct child of Enemy()

class Armour(Enemy):
    def __init__(self):
        self.hp *= 1.25
        self.armour *= 1
        self.description = "The enemy apears to be hatches down in some sort",\
            " of armoured vehicle"


""" TODO: add functions to dissmounts to add more armour if they have some
    sort of cover ie. OHP, Trenches. Possibliy cover can be chosen from a
    list of covers"""


class Dissmounts(Enemy):  # No armour unless under cover.
    def __init__(self, cover=None):
        self.hp *= 0.5
        self.armour = 0
        self.description = "Enemy soldiers. Basic grunts. Very vulnerable",\
            " in the open but harder to kill once dug-in."


""" These 3 are direct from Armour(). Armour is being multiplied by a set
    value. Might be a better way of doing this."""


class AntiAir(Armour):
    def __init__(self):
        self.armour *= 0.5
        self.description = "It's a enemy air defence vehicle! This should ", \
            "be a top priority kill."


class MBT(Armour):
    def __init__(self):
        self.armour *= 1.25
        self.description = "Enemy MBT out of concealment! Prime target for ",\
            "the Guns!"


class Recce(Armour):
    def __init__(self):
        self.armour *= 0.75
        self.description = "Light and fast, recce vehicles aren't ",\
            "made to take a hit."
