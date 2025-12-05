# Overloading 
class MathOps:
    
    def add(self,a,b):
        return a + b
    
    def add(self,a,b,c):
        return a + b + c 

obj = MathOps()
# print(obj.add(10,20)) # TypeError: MathOps.add() missing 1 required positional argument: 'c'
print(obj.add(10,20,30))


# A way around to simulate overloading but not really overloading -> python technique 
class Math:
    def add(self,a=0,b=0,c=0):
        return a + b + c 

obj = Math()
print(obj.add(10,20))
print(obj.add(10,20,30))