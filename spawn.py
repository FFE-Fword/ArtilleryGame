import random
import npc

# Lists in military breakdown style, a(Armoured) or i(Infantry)

a_comp = []
i_comp = []
a_plt = []
i_plt = []
a_trp = []
i_sec = []

# Creates an instance of enemies and assigns them to a variable

en_diss = npc.Grunt()
en_recce = npc.Recce()
en_anti = npc.AntiAir()
en_arm = npc.Armour()

def spawn_sec():
        for i in range(10):
                i_sec.append(en_diss)
        return i_sec

# Use .cout to find occurance in list

def is_sec(list):
        return list.count(en_diss) >=10
                
spawn_sec()
print(i_sec)
print(is_sec(i_sec))