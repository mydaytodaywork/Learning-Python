#contains only one copy of an element
#removes the duplicate{}

sett={"Kamal","Kamal","Happy"}
print(sett)

#We can perform union, subtraction, intersection, etc.
even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)

# union: numbers which are big or even
print(big_numbers | even_numbers)

# intersection: numbers which are big and even
print(big_numbers & even_numbers)

# numbers which are in big or even but not both
print(big_numbers ^ even_numbers)
