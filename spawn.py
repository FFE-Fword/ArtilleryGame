import random
import npc

# Lists in military breakdown style, a(Armoured) or i(Infantry)

a_pltplus = False
i_pltplus = False
a_trpplus = False
i_secplus = False
a_coy = False
i_coy = False
a_plt = False
i_plt = False
a_trp = False
i_sec = False
a_coyminus = False
i_coyminus = False
a_pltminus = False
i_pltminus = False
a_trpminus = False
i_secminus = False

# List of enemies

enemy = []

# Creates an instance of enemies and assigns them to a variable

en_diss = npc.Grunt()
en_recce = npc.Recce()
en_anti = npc.AntiAir()
en_arm = npc.Armour()

# Spawns a random amount of enemy Grunts() up to a company(128)

def spawn_en():
        for i in range(random.randint(1,128)):
                enemy.append(en_diss)
        return enemy

# Use .count to find occurance in list and changes enemy sizes to True if they 
# meet the requirements. Works, could use some cleaning.

def find_diss_size(list):
        if list.count(en_diss) == 128:
                i_coy = True
                print("It's a coy")
        elif list.count(en_diss) > 50 and list.count(en_diss) <= 127:
                i_coyminus = True
                print("It's a coy minus")
        elif list.count(en_diss) <= 49  and list.count(en_diss) >= 33:
                i_pltplus = True
                print("It's a plt plus")
        elif list.count(en_diss) == 32:
                i_plt = True
                print("It's a plt")
        elif list.count(en_diss) <=31 and list.count(en_diss) >= 16:
                i_pltminus = True
                print("It's a plt minus")
        elif list.count(en_diss) <=15 and list.count(en_diss) >= 9:
                i_secplus = True
                print("It's a sec plus")
        elif list.count(en_diss) == 8:
                i_coyminus = True
                print("It's a sec")
        elif list.count(en_diss) <=7 and list.count(en_diss) >=1:
                i_secminus = True
                print("It's a sec")
        else:
                print("There are no enemies. Continiue watching your arcs!")

spawn_en()
find_diss_size(enemy)

