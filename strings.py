name="kamal agrawal"

#Note: These slicing texchinques can also be used for array i.e. lists

#print(name[1])
#print(name[-1])  #indexing from end
#print(name[1:4])    #starting from one till end-1..3 here
#print(name[1:]) # 1 TO END
#print(name[:3]) # beg to end-1.. 2 here

#print(name.capitalize())    #initcap
#print(name.lower())     
#print(name.swapcase())      #swaps from l to u and u to l
#print(name.title())         #init cap each word
#print(name.upper())
#print(name)
#print(name.strip())         #strips the spaces from the begginning and the end
#print(name.strip(' '))      #we can specify the char here
#print(name.lstrip(' '))      #affects leading character only
#print(name.rstrip(' '))      #affects trailing character only

#print(name.replace('a','p'))    #repalces a with p  --- replaces a string
#print(name.replace('a','p',2))    #repalces a with p 2 times only as specified

#print(name.replace('a',''))     #to remove characters


newstring="Kamal,Happy,Kamal"
names=(newstring.split(','))        #split by , and put in a list for further processing
#for x in names:
#    print(x)

#print(newstring.find(','))      #to search for some characters-- returns first occurence

newnames=["Kamal","Happy","Chirag"]
mystr=','.join(newnames)      #to join the strings
print(mystr)


