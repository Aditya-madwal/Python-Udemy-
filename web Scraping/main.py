from bs4 import BeautifulSoup

with open("web.html", mode='r') as file:
    text = file.read()
# here we have retrieved the whole code as a text
# print(text)

mySoup = BeautifulSoup(text, 'html.parser')
# object mySoup created
# html.parser tells whether it is html file or xml file

# now the object mySoup has attributes like title , body ,etc
# we can call them individually
# calls the whole line ALONG WITH THE TAGS

title_of_file = mySoup.title
print(title_of_file)  # gives the whole line along with the tags

print(title_of_file.string)
# gives the string inside the title only

# editing the title content :
title_of_file.string = "aditya has changed the string"
print(title_of_file.string)

print("-----------------------------")

print(
    mySoup.prettify())  # this prettify() function gives out the text in more beautiful way...tags written in seperate lines

print(mySoup.a)  # this gives the first line holding an attribute tag

# HOW TO USE ALL THE TAGS OF SAME KIND FROM THE HTML FILE

list_of_all_para = mySoup.findAll(name="a")
print(list_of_all_para)  # this returns the list of all the anchor tags lines (along with the tags)

# now this list can be operated as an ordinary list

for i in list_of_all_para:
    print(i)  # this gives the lines along with TAGs one by one
    print(i.getText())  # this gives the text (string) of all the lines one by one
    print(i.get("href"))  # this gives the link of every anchor tag one by one
    # just like HREF any attribute can be taken out
    pass

# to get a tag by its ID

heading1 = mySoup.find(name="h1", id="name")
print(heading1)

# to get a tag by its class

heading3 = mySoup.find(name="h3", class_="heading")  # since class is a reserved keyword thus class_ is used.
print(heading3)
# getting the class attribute of the heading3

class_of_heading3 = heading3.get("class")
print(class_of_heading3)  # this gives the list of class ['heading']

# selecting an item through the CSS SELECTORS :

facebook_url = mySoup.select_one(selector="p a")  # this gives the FIRST MATCHING ITEM IN THE LIST
# facebook_url = mySoup.select(selector="p a")  # this gives all the matches in the html file
print(facebook_url)

# another use at selectors :
head1 = mySoup.select_one("#name")  # since heading 1 has the id = name
#  or
head1 = mySoup.select_one(selector="#name")  # since heading 1 has the id = name
print(head1)
