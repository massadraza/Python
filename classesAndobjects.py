class Robber:
    life = 100

    def attack_robber(self):
        print ('Ouch, but that aint gonna stop me') 
        self.life -= 25  

    def health_status(self): 
        if self.life <= 0: 
            print ("WASTED") 
        else: 
            print (str(self.life) + " health left")

robber1 = Robber() 


robber1.attack_robber() 
robber1.health_status() 

    