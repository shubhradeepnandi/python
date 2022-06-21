#loop it 6 times
i = 1
while i < 6:
    print(i)
    i+=1

#Exit the while loop when  i is 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1

#Continue the while loop when  i is 3
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#While else statement
i =1
while i < 6:
    i += 1
    print(i)
else:
    print("The Value of i is more than 6")


#Loop through Items
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print (item)

#Terminate the Loop once a condition is met
for item in fruits:
    if item == "banana":
        break
    else:
        print (item)


#Escape the item when met
print('#######')
for item in fruits:
    if item == 'apple':
        continue
    print(item)

#Function of Pass

for item in fruits:
    pass
print("Text")