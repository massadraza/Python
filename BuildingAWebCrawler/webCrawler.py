import requests 
from bs4 import BeautifulSoup 


def item_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.ebay.com/e/_electronics/best-of-tech-deals/cell-phones-accessories/15032?_pgn=' + str(page)      
        source_code = requests.get(url) 
        plain_text = source_code.text 
        soup = BeautifulSoup(plain_text,features="html.parser")  
        for link in soup.findAll('a', {'class': 's-item__link'}):  
            print (link.h3.get_text()) 
            print (link["href"]) 
            #get_item_info(soup)           
        page += 1


def get_item_info(item_url):
    source_code = requests.get(item_url)  
    plain_text = source_code.text 
    soup = BeautifulSoup(plain_text,features="html.parser")
    for item_name in soup.findAll('h1', {'class': 'it-ttl'}):
        print (item_name.string)   
    for link in soup.findAll('h1'):
        print (link["href"])

item_spider(1)  

# Building a WebCrawler using Python code  