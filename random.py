import random

#float betweeen 0 and 1 excluding 1
print(random.random())

my=["Kamal","KAMAL","hAPPY"]
#print(my)

#shuffles a list inplace
random.shuffle(my)
#print(my)

#randomly selects an element
print(random.choice(my))

#int rand
print(random.randint(1,10))

#seed with a diff value as it does wrt clock
random.seed(10)
print(random.random())
