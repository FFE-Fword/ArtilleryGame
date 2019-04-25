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
i_sec = False
a_coyminus = False
i_coyminus = False
a_pltminus = False
i_pltminus = False
a_trpminus = False
i_secminus = False
a_1x = False
i_1x =False

# List of enemies

enemy = []

# Creates an instance of enemies and assigns them to a variable

en_diss = npc.Grunt()
en_recce = npc.Recce()
en_anti = npc.AntiAir()
en_arm = npc.Armour()

# Spawns a random amount of enemies

def spawn_diss():
        for i in range(random.randint(1,128)):
                enemy.append(en_diss)
        return enemy

def spawn_recce():
        for i in range(random.randint(1,16)):
                enemy.append(en_recce)
        return enemy

def spawn_arm():
        for i in range(random.randint(1,16)):
                enemy.append(en_arm)
        return enemy

def spawn_anti():
        for i in range(random.randint(1,5)):
                enemy.append(en_anti)
        return enemy

# Use .count to find occurance in list and changes enemy sizes to True if they 
# meet the requirements. Works, could use some cleaning.


# Working like expected. Take another look.

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
                i_sec = True
                print("It's a sec")
        elif list.count(en_diss) <=7 and list.count(en_diss) >=1:
                i_secminus = True
                print("It's a sec")
        else:
                print("There are no enemies. Continiue watching your arcs!")


# Working like expected. Take another look.

def find_recce_size(list):        
        if list.count(en_recce) >=13 and list.count(en_recce) <=16:
                a_pltplus = True
                print("It's a coy plus of armoured")
        elif list.count(en_recce) ==12:
                a_coy = True
                print("It's a coy of  armoured recce")
        elif list.count(en_recce) >= 8 and list.count(en_recce) <=11:
                a_coyminus = True
                print("It's a coy minus of armoured recce")
        elif list.count(en_recce) >=4 and list.count(en_recce) <= 7:
                a_pltminus = True
                print("It's a plt plus of armoured recce")
        elif list.count(en_recce) ==3:
                a_plt = True
                print("It's a plt")
        elif list.count(en_recce) == 2:
                a_pltminus = True
                print("It's a plt minus")
        elif list.count(en_recce) == 1:
                a_1x = True
                print("It's 1x recce vehicle")
        else:
                print("There are no enemies. Continiue watching your arcs!")

# Working like expected. Take another look.

def find_arm_size(list):        
        if list.count(en_arm) >=13 and list.count(en_arm) <=16:
                a_pltplus = True
                print("It's a coy plus of armour")
        elif list.count(en_arm) ==12:
                a_coy = True
                print("It's a coy of armour")
        elif list.count(en_arm) >= 8 and list.count(en_arm) <=11:
                a_coyminus = True
                print("It's a coy minus of armour")
        elif list.count(en_arm) >=4 and list.count(en_arm) <= 7:
                a_pltminus = True
                print("It's a plt plus of armour")
        elif list.count(en_arm) ==3:
                a_plt = True
                print("It's a plt of armour")
        elif list.count(en_arm) == 2:
                a_pltminus = True
                print("It's a plt minus of armour")
        elif list.count(en_arm) == 1:
                a_1x = True
                print("It's 1x armoured vehicle")
        else:
                print("There are no enemies. Continiue watching your arcs!")

spawn_diss()
spawn_recce()
spawn_arm()
find_diss_size(enemy)
find_recce_size(enemy)
find_arm_size(enemy)
