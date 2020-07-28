Students_in_class = [28, 26, 30, 45]

def new_students(students):
    return students * 2

new_students_list = list(map(new_students, Students_in_class))
print (new_students_list) 

# Learning about the map function 