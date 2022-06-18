#Get the character at position 1 of a String
def characterOne(string):
    return characterOne[0]

#Loop through a String
string="Absolutely Long String"
for item in string:
    print(item)

#Find the length of a string
print(len(string))

#Find a certain phrase within a string
string = "The best things in life are free!"
print("free" in string)

#extract 'llo' from the below string
txt = "Hello World"
print(txt[2:5])

#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
print(txt.strip())

#Convert the value of txt to upper case.
txt = "Hello World"
print(txt.upper())

#Convert the value of txt to lower case.
txt = "Hello World"
print(txt.lower())

#Replace the character H with a J.
txt = "Hello World"
print(txt.replace('H', 'J'))

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))