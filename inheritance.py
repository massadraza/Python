class Parent(): 

    def last_name(self): 
        print('Raza') 

class Child(Parent):
    
    def first_name(self): 
        print('Massad') 
    # Over riding inheritance 
    def last_name(self): 
        print('Python') 

massad = Child() 
massad.first_name()
massad.last_name() 

# Learning what inheritance is in Python and how to over ride inheritance  