import requests
from bs4 import BeautifulSoup
import operator 

def start(url):
    word_list = []
    source_code = requests.get(url).text 
    soup = BeautifulSoup(source_code, features="html.parser") 
    for post_text in soup.findAll('a', {'class': "style-scope ytd-comment-renderer"}):
        content = post_text.string 
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list) 

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='" 
        for x in range(0, len(symbols)): 
            word = word.replace(symbols[x], "") 
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)


start('https://www.youtube.com/watch?v=ZxiJ92-4Qys&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=36&t=70s')

# Building a Word Frequency Counter using Python Code