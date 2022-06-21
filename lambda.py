# Simple Lambda Function
x = lambda a: a+5
print(x(3))

#Multiply agrument a,b,c and return result
y = lambda a,b,c:a*b*c

print(y(3,5,7))

#Summarize the argument a,b,c and return result

z = lambda a,b,c: a+b+c
print(z(1,2,3))


#Define lambda function that multiples(double, trebble)
def func(n):
    return lambda a : a*n

doublefunc = func(2)
tripplefunc = func(3)

print(doublefunc(4))
print(tripplefunc(4))

