from npc import *


tsevtwo = MBT()
zsu = AntiAir()
brdm = Recce()
nazis = Dissmounts()

print(nazis.base_armour)
print(nazis.base_hp)
nazis.take_damage(1)
print(nazis.base_hp)
print(nazis.base_armour)
nazis.take_damage(100)
print(nazis.base_hp)
print(nazis.base_armour)
print(nazis)
print(zsu)
