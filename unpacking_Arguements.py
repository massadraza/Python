def hours_spent_sleeping(time_woken, time_slept, total_hours): 
    answer = (100 - time_woken) + ( 65 - time_slept) - ( 75 - total_hours) 
    print(answer , "years old expected") 
    

massads_results = [9, 10, 11] 
hours_spent_sleeping(massads_results[0], massads_results[1], massads_results[2]) 
hours_spent_sleeping(*massads_results) 

#Learning how to unpack Arugements 






