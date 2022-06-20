#create a tupple
thistupple = ("apple", "Bananna", "Cherry")
print(thistupple)

print(thistupple[0])
print(thistupple[1])
print(thistupple[2])

print(len(thistupple))

#create a tupple with one item
oneTupple = ('apple',)
print(oneTupple)

print(thistupple[1:])

#how to update tupple values
tempList = list(thistupple)
tempList[0]="Plum"
thistupple = tuple(tempList)
print(thistupple)

#Adding values to Tupple
tempList = list(thistupple)
tempList.append("Grapes")
thistupple = tuple(tempList)
print(tempList)

#Adding Tupple to Tupple
thistupple = thistupple + oneTupple
print(thistupple)

#Remove Items from tupple
tempList = list(thistupple)
tempList.remove("apple")
tempList.pop(1)
thistupple = tuple(tempList)
print(thistupple)

#Unpacking a Tupple
plum,cherry,grapes = thistupple
print(plum)
print(cherry)
print(grapes)

plum,*other = thistupple
print(plum)
print(*other)

#loop tupples
for item in thistupple:
    print(item)
for x in range(len(thistupple)):
    print(x,":",thistupple[x])

#Join two tupple
print(thistupple + thistupple)
print(thistupple * 2)
