import random 
import urllib.request 

def download_image(url):
    name = random.randrange(1,500)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name) 

download_image('https://www.python.org/static/community_logos/python-logo-master-v3-TM.png') 

# Learning how to download images from the internet using Python Code. 