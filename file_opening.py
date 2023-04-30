print("hehe open up that file")

sample_file = open("sample_text.txt")

text_in_the_file = sample_file.read()
# this simply reads the content in the file as string.

print(text_in_the_file)
# prints the content of the file


sample_file.close()
# closes the file which is opened in the backend

# to avoid closing the file :-

with open("sample_text.txt", mode='w') as sample_file:
    # w stands for write (we can edit the file ACTUALLY REPLACE THE TEXT WITH THE ONE WE ARE WRITING)
    # r would have stood for readOnly (no editing)
    # content = sample_file.read()
    # print(content)
    sample_file.write("\nThis text has been added by the WRITE() function.")
# print(data)
# now no need to close the file 
print("---------------------------------")

with open("sample_text_2.txt", mode='a') as sample_file_2:
    # a stands for append (adding text without harming the previous text)
    sample_file_2.write("\nthis is the appended text.")

# creating a new file

with open("created_file.txt", mode='w') as created_file:
    created_file.write("this file has been created by the python prgram.")

# this creates a file named created_file.txt and writes the above text in it.

# readlines() Method :

name_for_merging = open('name_for_merging.txt', mode='r')
list_of_names = name_for_merging.readlines()  # converts the data line by line as a list
print(list_of_names)
