#Note: We cannnot refer to global and local variable both in the same function
#the following fucntion generates error if we use 1st stataemnt.. as we are accessing global and then creating a local variable.

#Hence use passing of values is preferable
a = 0
def my_function():
    #print(a)
    a = 3
    print(a)

my_function()



#function can return multiple values
def hello(text,count):
    print(text*count)
    return 3,5

#p,q=hello("Kamal",2)
#print(p+q)

#concepts

# 1. variables used inside function are local variables unless global keyword is used
# try removing global and check the output it will be different

x=3
def test():
    global x
    x=5
test()
print(x)

#another multiple return example
def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# you can do this
q, r = divide(35, 4)

# but you can also do this
result = divide(67, 9)
q1 = result[0]
q2 = result[1]
