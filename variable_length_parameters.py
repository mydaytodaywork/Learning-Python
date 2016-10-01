# We can mix ordinary parameters, *args and **kwargs in the same function definition.
# *args and **kwargs must come after all the other parameters, and **kwargs must come after *args.

def print_args(*args):      # * is used for passing variable length list
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):     # ** is used for passing dictionary
    for k,v in kwargs.items():
        print("%s: %s" % (k, v))

print_args("one", "two", "three")
print_args("one", "two", "three", "four")

print_kwargs(name="Jane", surname="Doe")
print_kwargs(age=10)
