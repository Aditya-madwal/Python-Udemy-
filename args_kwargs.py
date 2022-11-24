print("args and kwargs")

# *ARGS :

def sample_func(*args) :
    # this *args argument allows us to write the code without worrying anout the number of variables we can pass.
    # here the args is a tuple of all the inputs inputed as arguments
    print(args)
    for i in args :
        print(i)

def add(*numbers) :
    sum_of_numbers = 0    
    for n in numbers :
        sum_of_numbers += n
    print(sum_of_numbers)   


sample_func(1,2,3,2,4)

add(1,2,3,4,5,6,7,8,9)

def sample_func_2(*items) :
    print(items)
    name = items[2]
    print(f"item at the index no.2 is {name}")

    # suming up the numbers in the items 
    sum_of_integers = 0
    for number in items :
        if type(number) == int :
            sum_of_integers += number
    print(sum_of_integers)

sample_func_2(2,5,"aditya",True)

# **KWARGS :

def sample_kwarg_func(**kwargs) :
    # here the kwargs is a dictionary 
    print(kwargs)
    # to individually deal with the arguments inside the dictionary :
    for key,value in kwargs.items() :
        print(key)
        print(value)
    
    aditya_rollcall = kwargs['rollcall']
    print(f"aditya's rollcall is {aditya_rollcall}")

sample_kwarg_func(name = 'aditya' , rollcall = 3)
# 'name' is a keyword argument and 'aditya' is the key value 
# prints {'name' : 'aditya' , 'rollcall' : 3}
    


