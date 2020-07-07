import requests 
from bs4 import BeautifulSoup 


def item_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.ebay.com/e/_electronics/best-of-tech-deals/cell-phones-accessories/15032?_pgn=' + str(page)      
        source_code = requests.get(url) 
        plain_text = source_code.text 
        soup = BeautifulSoup([plain_text], "html.parser")  
        for link in soup.findAll('a', {'class': 's-item__title'}): 
            h3 = "https://www.ebay.com" + link.get('h3')
            title = link.string 
            print (h3)
            print (title) 
        page += 1



item_spider(1) 