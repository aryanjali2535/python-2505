# Overriding 

class Animal:
    def sound(self):
        print("Parent Animal Sound")

class Dog(Animal):
    def sound(self): # override
        print("Dog Makes Woff")
        
class Cat(Animal):
    def sound(self): # override
        print("Cat Makes Meow")

class Cow(Animal):
    def sound(self): # override
        print("Cow Makes Mooo")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()
cat = Cat()
cat.sound()
cow = Cow()
cow.sound()