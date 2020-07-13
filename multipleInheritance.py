class car_move(): 

    def gas(self):
        print ('Accelerating') 

class car_stop():

    def slow(self):
        print ('Slowing down')

class car_drift(car_move, car_stop):
    print ('Drifiting') 
# If you have nothing to put in this class just write pass to avoid syntax errors.

dr = car_drift()
dr.gas()
dr.slow() 

# Learning about how to inherit multiple classes at once. 