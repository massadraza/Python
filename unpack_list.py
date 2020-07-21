def final_avg(grades): 
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print (avg)  

final_avg([64, 78, 54, 56, 42])  

# Learning how to unpack lists and what are tuples