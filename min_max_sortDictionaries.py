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

print(sorted(zip(Stock.keys, Stock.values()))) 
print(min(zip(Stock.keys, Stock.values()))) 
print(max(zip(Stock.keys, Stock.values())))  

# Learning how to organize a dictionary and sort it in min, max, sort.