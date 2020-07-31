Stock = {
        'NASDAQ': 10680.36,
        'NYSE': 12508.68,
        'Dow Jones': 26840.40,
        'APPL': 388.00,
        'SBUX': 75.44,
        'NKE': 98.36,
        'TMUS': 105.58,
        'AMZN': 3138.29,      

} 

min_price = min(zip(Stock.values(), Stock.keys())) 
max_price = max(zip(Stock.values(), Stock.keys())) 
print(min_price)
print(max_price) 

# Learning how to print the min and max values from a list.

