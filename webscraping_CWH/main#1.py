print("web scraping using python")

#------------------------------------------------------------------------------
# step 0
# import all requirements 

from bs4 import BeautifulSoup
import html5lib
import requests

#------------------------------------------------------------------------------
# step 1
# get the html file 

url = "https://codewithharry.com"

r = requests.get(url)
# r is the requested url

html_content = r.content
# the whole html code is now in the html_content
# print(html_content) # prints the whole html code without indentations

#------------------------------------------------------------------------------
# step 2
# parse the html 

soup = BeautifulSoup(html_content,'html.parser')
print(soup) # prints the whole html code 
print(soup.prettify()) # prints the whole html code with indentations (prettified manner)


#------------------------------------------------------------------------------ 
# step 3
# html tree traversal

print(soup.get_text()) # prints only the text of the html file (headings, para, etc)

