print("this is a mail merging project-")
print("TODO - pick the names from names_for_merging.txt individually and replace the [name] in the example.txt with the names")

# replace() Method :

# txt = 'i love shaxpeur'
# print( txt.replace('shaxpeur' , 'chetna') )

# readlines() Method :

text = "the name is [name]."

example_text = open("example_mail.txt", mode='r')
mail_content = example_text.read()
print(mail_content)

name_for_merging = open('name_for_merging.txt', mode='r')
# names = name_for_merging.read()
# print(names)
# list_of_names = name_for_merging.readlines()
list_of_names = name_for_merging.readlines()
print(list_of_names)

for name in list_of_names:
    stripped_name = name.strip()
    final_mail_content = mail_content.replace('[name]', stripped_name)
    print(final_mail_content)
    with open(f"{stripped_name}_mail.txt", mode='w') as new_file:
        new_file.write(final_mail_content)

# this creates text files named after all the names from the file.
