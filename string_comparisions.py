name1="Kamal"
name2="kamal"
name3="123"

if(name3.isalpha()):
    print(name3 + " is alpha")
else:
    print(name3 + " is a number")

if(name2.isalpha()):
    print(name2 + " is alpha")
else:
    print(name2 + " is a number")

# other functions are isalnum, isdigit, islower, isupper, isspace, istitle

#startswith
if(name2.startswith('k')):
    print("That starts with K")

#endswith
if(name2.endswith('l')):
    print("That ends with l")
