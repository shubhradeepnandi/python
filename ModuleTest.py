import greetModule

def greet(name):
    greetModule.greetHello(name)
    greetModule.greetBye(name)
    print(greetModule.person1['age'])

greet('kali')


#Built in Modules

import platform

print(dir(platform))
print(platform.version())