#Create a List
thislist = ["apple", "banana", "cherry"]

#Length of the list
print(len(thislist))

#Access List Items

#Direct from Front
print(thislist[0])
#Negative Index
print(thislist[-1])
#Range Of Items
print(thislist[-3:])
#Check if an item in list
print('apple' in thislist)


#Change values in the list
thislist[-1] = 'Blueberry'

thislist[1:2] = ["Bread", "eggs","butter"]
print(thislist)

#Add Items to the List
#1.Append Items to the List
thislist.append('Bananna')
print(thislist)

#2.Insert Items to the list
thislist.insert(3,'watermelon')
print(thislist)

#3.Extend the list
thislist.extend([ 'Chicken', 'eggs', 'fish'])
print(thislist)

#Remove/Delete Item from the List
#thislist.remove('eggs')
#del thislist[0]
#thislist.pop(2)
#thislist.clear()
print(thislist)

#List Comprehension
newlist = [x.upper() for x in thislist if x not in ['eggs','Chicken', 'fish']]
print(newlist)

#sort the list
newlist.sort()
print(newlist)
  #Reverese
newlist.sort(reverse=True)
print(newlist)
  #Custom Sort Function
def mySort(n):
    return abs(n-50)

listNew = [23,95,46,37,105,53]
listNew.sort(key = mySort)
print(listNew)

#Copy Lists
litsNew2 = listNew.copy()
litsNew2[3] = 45
print(listNew)
print(litsNew2)


