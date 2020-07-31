from operator import itemgetter 

Stock = [
        {"fname" : 'Amanda', 'lname': "Roberts"},
        {"fname" : 'Bobby', 'lname' : "Williams"},
        {"fname" : 'John', 'lname' : "Allen"},
        {"fname" : 'Elon', 'lname' : "Williams"},
        {"fname" : 'Don', 'lname' : "Jones"},
        {"fname" : 'Bobby', 'lname' : "Allen"},
        {"fname" : 'Nick', 'lname' : "Hayes"},
        {"fname" : 'Bobby', 'lname' : "Jones"},      

] 

for x in sorted(Stock, key=itemgetter('fname', 'lname')):  
    print(x) 

# Learning how to organize a list with multiple key sort. 
