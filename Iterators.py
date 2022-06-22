# Technically in python an Iterator
# is an object that implements the iterator protocol which consists of two methods
#__iter__() and __next__()

#String, List, Tuples, Set and Dictionary are Iterable Objects which you can get iterator Objects
myTupple = ('Item1', 'Item2', 'Item3')
myIter = iter(myTupple)

print(next(myIter))
print(next(myIter))
print(next(myIter))

myString = 'Banana'
myIter = iter(myString)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

#Create a Custom Iterator Class that starts from 100 and increments with multiple of 10

class NewNumber:
    def __iter__(self):
        self.a = 100
        return self
    def __next__(self):
        self.a+=10
        return self.a

number = NewNumber()
myIter = iter(number)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

for item in number:
    if item > 200:
        break
    else:
        print(item)




