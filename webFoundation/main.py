# web foundation #1

# bs4 stands for beautiful soup :
from bs4 import BeautifulSoup

with open(website.html) as file : 
    content = file.read()

soup = BeautifulSoup() 
# created an onject named soup
