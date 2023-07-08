#!/usr/bin/python3
class Pet:

    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def show(self):
        print(f" I am {self.name} and I am {self.age} years old\n")
class cat(Pet):
    def speak(self):
        print("I can meow")

class dog(Pet):
    def speak(self):
        print(" I bark at night")

p = Pet('tim', 8)
p.show()
c = cat('mauwa', 2)
c.show()
c.speak()

d = dog('Bosco', 4)
d.show()
d.speak()
