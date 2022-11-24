print("functions with some output")


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you left something empty"
    else:
        formated_fname = f_name.title()
        formated_lname = l_name.title()
        # title() function capitals the first letter of the name
        print(f"{formated_fname} {formated_lname}")


first_name = input("first name : \n")
last_name = input('last name : \n')
format_name('aditya', 'madwal')
print(format_name(first_name, last_name))


def confess(her_name):
    return f"ILY {her_name}"  # end of the function
    return "balle balle"  # not valued
    return "shaxpeur"  # not valued


confession = confess("chetna mehta")
print(confession)

