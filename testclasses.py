# Getting Class inheritance to work properly

class Enemy():  # All enemies a derived from this class
    
    base_hp = 100
    base_armour = 100
    description = ("An enemy of Canada that must not be allowed"
    " to live!!!")

    def __str__(self):
        return "{}".format(self.description)  
        
class Armour(Enemy):
       def __init__(self):
               super().__init__() 
               self.base_hp *= 1.25
        
class MBT(Armour):
    def __init__(self):
        super().__init__()
        self.base_armour *= 1.25
        self.description = ("Enemy MBT out of concealment! Prime target for"
            "the Guns!")

def check():
        tsevtwo = MBT()
        print(tsevtwo.base_armour)
        print(tsevtwo.base_hp)
        print(tsevtwo)
        return False

check()


        

  
        
  