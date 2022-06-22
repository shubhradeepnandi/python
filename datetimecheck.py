import datetime

print(datetime.datetime.now())

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

#Creating a datetime object

x = datetime.datetime(1984,2,25)

print(x)


print(x.strftime('%B'))
print(x.strftime('%A'))
print(x.strftime('%C'))
