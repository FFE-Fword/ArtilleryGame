import random

""" CLASSES work with basic functionality. Contains all enemy and friendly
classes. All based off Npc()They all have base variables of hp (health),
armour and a base description. When enemies take damage, their armour will
 deplete until 0, then hp will deplete."""


class Npc():

    base_hp = 100
    base_armour = 100
    description = ("Non Payer Contrlled")

    def __str__(self):
        return "{}".format(self.description)

# Function that checks if the damage taken will reduce self.armour below 0
# if it does, set self.armour=0 and take the remainder and sets it to
# self.hp

    def take_damage(self, damage):
        hp_damage = 0
        if (damage - self.base_armour) <= 0:
            self.base_armour -= damage
        elif (damage - self.base_armour) > 0:
            hp_damage = damage - self.base_armour
            self.base_hp -= hp_damage
            self.base_armour = 0
            if self.base_hp <= 0:
                self.base_hp = 0

    # Checks if enemy health is above 0

    def is_alive(self):
        return self.base_hp > 0

    # Takes in amount(amt) as an int and adds to self.base_armour

    def set_armour(self, amt):
        self.base_armour = amt
        return self.base_armour


class Enemy(Npc):  # All enemies a derived from this class

    def __init__(self):
        super().__init__()
        self.description = ("An enemy of Canada that must not be allowed"
                            " to live!!!")

# Armour, AntiAir and Dissmounts direct child of Enemy()


class Armour(Enemy):
    def __init__(self):
        super().__init__()
        self.base_hp *= 1.25
        self.description = ("The enemy apears to be hatches down in some"
                            "sort of armoured vehicle")


""" Added functions to dissmounts to add more armour if they have some
    sort of cover ie. OHP, Dug-in. Could possibly make this better"""


class Dissmounts(Enemy):  # No armour unless under cover.
    cover = ["In the Open", "Dug in", "Dug in with OHP"]

    def __init__(self, cvr=cover[0]):
        super().__init__()
        self.cvr = cvr
        self.base_hp *= 0.5
        self.base_armour = 0
        self.description = ("Enemy soldiers. Basic grunts. Very vulnerable"
                            " in the open but harder to kill once dug-in.")

    def has_cover(self, cvr=cover):
        degree = random.randint(0, 2)
        if degree == 1:
            print("They are: " + cvr[degree])
            self.base_armour += 15
        elif degree == 2:
            print("They are: " + cvr[degree])
            self.base_armour += 25
        else:
            print("They are: " + cvr[degree])


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


#############################
#############################

"""Working. Needs works still. All friendly classes below. None of them have base armour since they would not be dug in...and we all know it!!"""

class Friendly(Npc):
    def __init__(self):
        super().__init__()
        self.base_armour = 0
        self.description = ("A friendly GBA+ qualified member of the"
                            " Canadian Armed Forces!")


class Heavies(Friendly):
    def __init__(self):
        super().__init__()
        self.description = ("A hard chargin', gravy chugin', Strat!")


class Grunt(Friendly):
    def __init__(self):
        super().__init__()
        self.base_hp *= 0.5
        self.description = ("Your friendly neighbourhood Patricia")


class Guns(Friendly):
    def __init__(self):
        super().__init__()
        self.base_hp *+ 0.2
        self.description = ("Friendly artillery piece. Manned by the finest "
                            "gunners in 1RCHA, and therefore the world.")



nazis = Dissmounts()
comeau = Heavies()

print(nazis.base_armour, nazis.base_hp)
nazis.has_cover()
print(nazis.is_alive())
nazis.take_damage(30)
print(nazis.base_armour, nazis.base_hp)
nazis.take_damage(100)
print(nazis.is_alive(), "\n")

print(comeau.base_armour, comeau.base_hp)
print(comeau.is_alive())
comeau.take_damage(30)
print(comeau.base_armour, comeau.base_hp)
comeau.take_damage(100)
print(comeau.is_alive())
print(Friendly())