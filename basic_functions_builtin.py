# 0 and empty string are considered as false values
values=["Frue",4,5,0]
#are any of the value true
print(any(values))


#are all of the values true
print(all(values))

print('a' in 'abcd') # True
print('ab' in 'abcd') # also True

# this doesn't work for lists
print(['a', 'b'] in ['a', 'b', 'c', 'd']) # False

abc_list = list("abracadabra")
