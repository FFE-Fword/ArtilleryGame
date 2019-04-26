import random
import npc

# Setting enemy formation size in military breakdown style, a(Armoured) or i(Infantry); sec == section, plt == platoon, coy == company


a_coy = False
i_coy = False
a_coyminus = False
i_coyminus = False
a_pltplus = False
i_pltplus = False
a_plt = False
i_plt = False
a_pltminus = False
i_pltminus = False
i_secplus = False
i_sec = False
i_secminus = False
a_1x = False
i_1x =False

# List of enemies

enemy = []

# Creates an enemy and sets to a variable. For dissmounts, it adds a level
# of cover that all dissmounts will share. 

en_diss = npc.Dissmounts().has_cover()
en_recce = npc.Recce()
en_arm = npc.Armour()
en_anti = npc.AntiAir()

####This is the funtion that will shorten en generator

def spawn_en():
        
        for i in range(random.randint(1,128)):
                enemy.append(en_diss)
        for i in range(random.randint(1,16)):
                enemy.append(en_recce)
        for i in range(random.randint(1,16)):
                enemy.append(en_arm)
        return enemy

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
# NOT WORKING AS EXPECTED, 
def find_en_size(list):
        spawn_en()
        if (en_diss and en_arm and en_recce) in enemy: # If diismounts, arm and 
                # recce are generated
                print("Enemy dissmounts sup by armour and armoured recce")
                if (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_arm) == 3) and (list.count(en_recce) == 3):
                        i_secplus, a_plt = True, True
                        print("It's a sec+ of diss sup by plt of arm and plt of recce.")
                elif (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_arm) == 2) and (list.count(en_recce) == 2):
                        i_secplus, a_pltminus = True, True
                        print("It's a sec+ of diss sup by plt- of arm and plt- of recce.")
                elif (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_arm) == 1) and (list.count(en_recce) == 1):
                        i_secplus, a_1x = True, True
                        print("It's a sec+ of diss sup by 1x arm and 1x recce.")
                elif list.count(en_diss) == 8 and (list.count(en_arm) == 3) and (list.count(en_recce) == 3):
                        i_sec, a_plt = True, True
                        print("It's a sec of diss sup by plt of arm and plt of recce.")
                elif (list.count(en_diss) == 8) and (list.count(en_arm) == 2) and (list.count(en_recce) == 2):
                        i_sec, a_pltminus = True, True
                        print("It's a sec of diss sup by plt- of arm and plt- of recce.")
                elif (list.count(en_diss) == 8) and (list.count(en_arm) == 1) and (list.count(en_recce) == 1):
                        i_sec, a_1x = True, True
                        print("It's a sec of diss sup by 1x arm and 1x recce.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_arm) == 3) and (list.count(en_recce) == 3):
                        i_secminus, a_plt = True, True
                        print("It's a sec- of diss sup by plt of arm and plt of recce.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_arm) == 2) and (list.count(en_recce) == 2):
                        i_secminus, a_pltminus = True, True
                        print("It's a sec- of diss sup by plt- of arm and plt- of recce.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_arm) == 1) and (list.count(en_recce) == 1):
                        i_secminus, a_1x = True, True
                        print("It's a sec- of diss sup by 1x arm and 1x recce.")
                
        elif en_diss and en_recce in enemy: # dissmounts and recce only
                if (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and  (list.count(en_recce) == 3):
                        i_secplus, a_plt = True, True
                        print("It's a sec+ of diss sup by a plt of recce.")
                elif (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_recce) == 2):
                        i_secplus, a_pltminus = True, True
                        print("It's a sec+ of diss sup by a plt- of recce.")
                elif (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_recce) == 1):
                        i_secplus, a_1x = True, True
                        print("It's a sec+ of diss sup by 1x recce.")
                elif list.count(en_diss) == 8 and (list.count(en_recce) == 3):
                        i_sec, a_plt = True, True
                        print("It's a sec of diss sup by plt of recce.")
                elif (list.count(en_diss) == 8) and (list.count(en_recce) == 2):
                        i_sec, a_pltminus = True, True
                        print("It's a sec of diss sup by plt- of recce.")
                elif (list.count(en_diss) == 8) and (list.count(en_recce) == 1):
                        i_sec, a_1x = True, True
                        print("It's a sec of diss sup by 1x recce.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_recce) == 3):
                        i_secminus, a_plt = True, True
                        print("It's a sec- of diss sup by plt of recce.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and(list.count(en_recce) == 2):
                        i_secminus, a_pltminus = True, True
                        print("It's a sec- of diss sup by plt- of recce.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_recce) == 1):
                        i_secminus, a_1x = True, True
                        print("It's a sec- of diss sup by 1x recce.")

        elif en_diss and en_arm in enemy: # dissmounts and arm only
                if (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and  (list.count(en_arm) == 3):
                        i_secplus, a_plt = True, True
                        print("It's a sec+ of diss sup by a plt of armour.")
                elif (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_arm) == 2):
                        i_secplus, a_pltminus = True, True
                        print("It's a sec+ of diss sup by a plt- of armour.")
                elif (list.count(en_diss) <=15 and list.count(en_diss) >= 9) and (list.count(en_arm) == 1):
                        i_secplus, a_1x = True, True
                        print("It's a sec+ of diss sup by 1x armour.")
                elif list.count(en_diss) == 8 and (list.count(en_arm) == 3):
                        i_sec, a_plt = True, True
                        print("It's a sec of diss sup by plt of armour.")
                elif (list.count(en_diss) == 8) and (list.count(en_arm) == 2):
                        i_sec, a_pltminus = True, True
                        print("It's a sec of diss sup by plt- of armour.")
                elif (list.count(en_diss) == 8) and (list.count(en_arm) == 1):
                        i_sec, a_1x = True, True
                        print("It's a sec of diss sup by 1x armour.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_arm) == 3):
                        i_secminus, a_plt = True, True
                        print("It's a sec- of diss sup by plt of armour.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and(list.count(en_arm) == 2):
                        i_secminus, a_pltminus = True, True
                        print("It's a sec- of diss sup by plt- of armour.")
                elif (list.count(en_diss) <=7 and list.count(en_diss) >=1) and (list.count(en_arm) == 1):
                        i_secminus, a_1x = True, True
                        print("It's a sec- of diss sup by 1x armour.")


        elif en_arm and en_recce in enemy: # recce and arm only
                if (list.count(en_recce) == 3) and  (list.count(en_arm) == 3):
                        a_plt = True
                        print("It's a plt of recce sup by a plt of armour.")
                elif (list.count(en_recce) == 3) and  (list.count(en_arm) == 2):
                        a_plt, a_pltminus = True, True
                        print("It's a plt of recce sup by a plt- of armour.")
                elif (list.count(en_recce) == 3) and  (list.count(en_arm) == 1):
                        a_plt, a_1x = True, True
                        print("It's a plt of recce sup by 1x armour.")
                elif list.count(en_recce) == 2 and (list.count(en_arm) == 3):
                        a_pltminus, a_plt = True, True
                        print("It's a plt- of recce sup by plt of armour.")
                elif (list.count(en_recce) == 2) and (list.count(en_arm) == 2):
                        a_pltminus = True
                        print("It's a plt- of recce sup by plt- of armour.")
                elif (list.count(en_recce) == 2) and (list.count(en_arm) == 1):
                        a_pltminus, a_1x = True, True
                        print("It's a plt- of recce sup by 1x armour.")
                elif (list.count(en_recce) == 1) and (list.count(en_arm) == 3):
                        a_1x, a_plt = True, True
                        print("It's a 1x recce sup by plt of armour.")
                elif (list.count(en_recce) == 1) and (list.count(en_arm) == 2):
                        a_1x, a_pltminus = True, True
                        print("It's a 1x recce sup by plt- of armour.")
                elif (list.count(en_recce) == 1) and (list.count(en_arm) == 1):
                        a_1x = True
                        print("It's a 1x recce sup by 1x armour.")
       

        else:
                print("There are no enemies. Continiue watching your arcs!")




      
find_en_size(enemy)

