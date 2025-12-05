# Types Of Inheritance 

# Single Level Inheritance : One Parent -> One Child 

class Father:
    def house(self):
        print("Has House")

class Son: # No Inheritance
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
# son_obj.house() # AttributeError: 'Son' object has no attribute 'house'

print("=" * 20)

# With Inheritance
class Son(Father): 
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()

print("=" * 20)

# Multi Level Inheritance : GrandParent -> Parent -> Child 
class GrandParent:
    def land(self):
        print("Has Agricultural Land")

class Father(GrandParent):
    def house(self):
        print("Has House")

class Son(Father): 
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()

print("=" * 20)

# Multiple Inheritance : One Child -> Multiple Parents 
class GrandParent:
    def land(self):
        print("Has Agricultural Land")

class Father(GrandParent):
    def house(self):
        print("Has House")

class Mother:
    def gold(self):
        print("Has Gold")

class Son(Father,Mother): # applying Multiple Inheritance
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()
son_obj.gold()

print("=" * 20)

# Hierarchial Inheritance : One Parent -> Multiple Child
class Father():
    def house(self):
        print("Has House")

class Son(Father): 
    def car(self):
        print("Has Car")

class Daughter(Father):
    def business(self):
        print("Has Business")

son_obj = Son()
son_obj.car()
son_obj.house()

daughter_obj = Daughter()
daughter_obj.business()
daughter_obj.house()

print("=" * 20)

# Hybrid Inheritance : Combination or two or more types 
class A:
    def featureA(self):
        print("Feature A")

class B(A):
    def featureB(self):
        print("Feature B")

class C(A):
    def featureC(self):
        print("Feature C")

class D(B,C):
    def featureD(self):
        print("Feature D")

obj = D()
obj.featureA()
obj.featureB()
obj.featureC()
obj.featureD()