class player_status:

    def __init__(self, x):
        self.energy  = x 

    def energy_info(self):
        print (self.energy)

massad = player_status(11)
massad.energy_info() 

# Learning what is init and what scenarios you need to use init in. 