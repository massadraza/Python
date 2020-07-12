class boy:

    gender = 'Male' 

    def __init__(self, name):
        self.name  = name

a = boy('Massad')
b = boy('Jack')
c = boy('bob')
print (a.gender)
print (b.gender)
print (c.gender) 
print (a.name)
print (b.name) 

# Learning the difference between a Class Variable and a Instance Variable