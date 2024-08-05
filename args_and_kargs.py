#Example no. 1
def example_function(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

example_function(1, 2, 3, a=4, b=5)


#***************************************************************
#Example no.2
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'Linked MAtrix')


#***************************************************************
#Example no.3
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Mr.', mid='Hamza', last='Farooqi')

#***************************************************************
#Example no.4
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
args = ("mr.", "hamza", "bilal")
myFun(*args)

kwargs = {"arg1": "firend1", "arg2": "forhead1", "arg3": "ndskjf"}
myFun(**kwargs)
