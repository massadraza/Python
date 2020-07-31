import heapq 


grades = [23, 65, 88, 25, 32 ]
print(heapq.nlargest(3, grades))
Stock = [
        {"ticker" : 'NASDAQ', 'price': 10680.36},
        {"ticker" : 'NYSE', 'price' : 12508.68},
        {"ticker" : 'Dow Jones', 'price' : 26840.40},
        {"ticker" : 'APPL', 'price' : 388.00},
        {"ticker" : 'SBUX', 'price' : 75.44},
        {"ticker" : 'NKE', 'price' : 98.36},
        {"ticker" : 'TMUS', 'price' : 105.58},
        {"ticker" : 'AMZN', 'price' : 3138.29},      

] 

print(heapq.nsmallest(2, Stock, key=lambda stock: stock['price'])) 
print(heapq.nlargest(2, Stock, key=lambda stock: stock['price']))    

# Learning how to find the largest and smallest items in a list.