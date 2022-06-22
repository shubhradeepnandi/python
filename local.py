#Local vs Global

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Global Keyword
x = 300

def myfunc():
  global x
  x = 200
  print(x)

myfunc()

print(x)