from urllib import request 

APPL_url = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1562188252&period2=1593810652&interval=1d&events=history'

def download_APPL_stock_info(csv_url):
    response = request.urlopen(csv_url)  
    csv = response.read() 
    csv = str(csv)
    lines = csv.split("\\n") 
    dest_url = r'APPL.csv' 
    fx = open(dest_url, 'w') 
    for line in lines:
        fx.write(line + "\n") 
    fx.close() 

download_APPL_stock_info(APPL_url) 

#  Downloading files from the web using Python Code