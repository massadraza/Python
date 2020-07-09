Studentidstaken = [ 5, 6, 8, 40, 31]
print ("These are your id numbers, please choose from the following that has not been taken!")

for n in range (1, 51):
    if n in Studentidstaken:
        continue
    print (n)

# Learning the keyword continue