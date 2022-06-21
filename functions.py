#Create a Function with a single name and print the name
def name(name):
    print(f'Name is {name}')

name('shubh')

#Create a function with arbitary arguments
def functArb(*args):
    argsize = len(args)
    print(argsize)
    for item in args:
        print(item)


functArb('grape', 'apple', 'mango')

#Create a keyword function with fname, lname, age

def cust(**kwargs):
    print(kwargs['fname'])
    print(kwargs['lname'])
    print(kwargs['age'])

cust(fname ='shub', lname='nondy', age='38')

#Default Parameter Values
def cname(name='Norway'):
    print('Country Name '+ name)

cname('India')
cname('Canada')
cname()

#Pass a List as argument, dictionary as argument to the same function
def funcVal(argument):
    print(str(type(argument)))
    if('list' in str(type(argument))):
        for item in argument:
            print(item)
    elif('dict' in str(type(argument))):
        for k,v in argument.items():
            print(k,' ',v)
    else:
        print(type(argument))


funcVal(['apple', 'banana', 'grapes'])
funcVal({'key1': 'banana', 'key2':'grapes'})

#Return Value from function
def threeTimes(x):
    return 3*x
print(threeTimes(3))
print(threeTimes(4))
print(threeTimes(5))

#Fibonacci Series using Recursion
#0 1 1 2 3 5 8 13 21 34

def fib(n):
    if(n<=1):
        return(n)
    else:
        return(fib(n-1)+fib(n-2))

print(fib(5))

def fact(n):
    k = 1
    if(n <=1):
        return 1
    else:
        return(n*fact(n-1))

print(fact(4))
