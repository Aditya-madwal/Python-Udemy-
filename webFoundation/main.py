# web foundation #1

# bs4 stands for beautiful soup :
from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# created an object named soup
print(soup.title)

