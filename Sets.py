#Create a Set of 5 Fruits
myfruitset = {'Banana', 'Cherry', 'Mango', 'Apple', 'Grapes'}

#Iterate through the set
for item in myfruitset:
    print(item)

#Find the Length of the Set
print(len(myfruitset))

#Add Items to the Set
myfruitset.add('jackfruit')

#Add items from another set
thisset = {"Egg", "Cheese", "Bread"}
myfruitsetnew = myfruitset.copy()
myfruitsetnew.update(thisset)
print(myfruitsetnew)

#Add items to the set from a list
thislist = ["Egg", "Cheese", "Bread"]
myfruitset.update(thislist)
print(myfruitset)

#Remove Item from Set
print(myfruitset.remove("Egg"))

print(myfruitset.discard("Egg"))
print(myfruitset)

myfruitset.pop()
print(myfruitset)

#Del to delete the set completely and clear to remove all elements fron the set

#Join two sets by creating a new set
newfruitset = {"crowfruit", 'cowfruit', 'yellowfruit'}
newset = myfruitset.union(newfruitset)
print(newset)

#Update the exising set by adding new items
myfruitset.update(newfruitset)
print(myfruitset)
