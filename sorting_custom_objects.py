from operator import attrgetter

class User:

    def __init__ (self, x, y):
        self.name = x
        self.user_experience = y

    def __repr__(self):
        return self.name + " : " + str(self.user_experience) +  'years of experience'

users = [
    User('Massad', 7),
    User('Don', 10),
    User('Sally', 6),
    User('Bobby', 1),
    User('Nick', 2),
    User('Brian', 5),
    User('Amanda', 3),
] 


for user in users:
    print(user) 

print('---------')
for user in sorted(users, key=attrgetter('name')):
    print(user) 

print('---------')
for user in sorted(users, key=attrgetter('user_experience')):
    print(user)  

# Learning how to sort custom objects by any attribute