#create a dictionary
thisDict = {"brand": "Ford", "Model": "Mustang", "Year" : 1964}

print(thisDict)

#Print the brand dictionary

print(thisDict["brand"])

#Print the dictionary length
print(len(thisDict))

#Get the model value
print(thisDict.get("Model"))

#Get all the keys
print(thisDict.keys())
print(thisDict.values())
print(thisDict.items())

#Access the Items
for item in thisDict.keys():
    print(thisDict.get(item))

for tup in thisDict.items():
    print(tup[0],tup[1])

#Change the value in dict year to 1998
thisDict["Year"] = 1998
print(thisDict)

#Update the dictionary by changing the Year to 2020

thisDict.update({"Year" :"2020"})
print(thisDict)

#Add Color to the dict

thisDict["Color"] = "Red"
print(thisDict)

#Remove Item Color from the Dict
thisDict.pop("Color") #Removes Color
thisDict.popitem() #Removes the last item
print(thisDict)

del thisDict['Model']
print(thisDict)

thisDict.clear()
print(thisDict)

#Create Dictionary
thisDict = {"brand": "Ford", "Model": "Mustang", "Year" : 1964}

#Loop Through the dictionary

for key, value in thisDict.items():
    print(key, value)

for item in thisDict.keys():
    print(item)

for item in thisDict.values():
    print(item)

#Copy dictionary

newDict = thisDict.copy()
print(newDict)

newDict = dict(thisDict)
print(newDict)

#Nested Dictionary of Employee List
emp1 = {"name" : "Akash", "empId" : "EMP001", "doj" : "12/03/20"}
emp2 = {"name" : "Akshay", "empId" : "EMP002", "doj" : "15/04/20"}
emp3 = {"name" : "Amit", "empId" : "EMP003", "doj" : "17/05/20"}

empDict = {"emp1" : emp1, "emp2" : emp2, "emp3": emp3}

print(empDict)