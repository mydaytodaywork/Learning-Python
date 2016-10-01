#used for hashing
student={"name":"Kamal","Branch":"Cse"}
student["roll"]="0089"
#del(student["name"])    #delete by key.. key can be multiple values
print(student)

#for x in student.keys():
#    print(x)

#for x in student.values():
#    print(x)

#check if a key exists
#if "name" in student:
#   print("Woe")

student.get("name")
# We can specify a different default
student.get("name", 0)

# Add several items to the dictionary at once
student.update({"name1": 34, "name2": 23, "name3": 36})

# All the keys in the dictionary
student.keys()
# All the values in the dictionary
student.values()
# All the items in the dictionary
student.items()


#use in and not in to check the presence of a key
#if x in ..
#if x not in ...
