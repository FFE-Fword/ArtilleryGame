class Enemy():  # All enemies a derived from this class

    def __init__(self,hp=100,armour=100,description=""):
        self.hp = hp
        self.armour = armour
        self.description = "An enemy of Canada that must not be allowed ",\
            "to live!!"

class Armour(Enemy):
       def __init__(self):
               super().__init__(self.hp,self.armour,self.description) 
                         
       
def check():
        tsevtwo = Armour()
        tsevtwo.armour
        print(tsevtwo.armour)
        return False

check()


        

  
        
  