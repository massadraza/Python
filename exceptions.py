while True:
    try:
        number = int(input('What is your favorite number? We will use this to detemine how long you will live!\n'))
        print(number/2 * 5) 
        break 
    except ValueError:
        print ('The following value entered is not a number! Please enter a number!')  
    finally: 
        print ("Thanks for trying our system out our system is still in beta testingee, if you are not happy with your results or the system please email us at massadraza@hotmail.com") 

#Learning how to ignore errors in Python Code by using exceptions
        