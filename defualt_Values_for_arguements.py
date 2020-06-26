def get_age(age = "Unknown"):
    if age is "13<":
        age = 'kid'
    elif age is "13>":
        age = 'teen'
    elif age is '18>':
        age = 'adult'
    print (age)

get_age('13<') 
get_age('13>')
get_age('18>') 
get_age()
