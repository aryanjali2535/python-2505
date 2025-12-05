# laptop contract (Govt said these are must for building laptops)

# With Abstraction (With Abstract Classes)

from abc import ABC, abstractmethod

class Laptop(ABC):
    
    @abstractmethod
    def processor(self):
        pass 
    
    @abstractmethod
    def ram_hdd(self):
        pass

# Implementations -> Laptop Manufactures 
class Lenovo(Laptop):
    
    def processor(self):
        print("Lenovo Laptop Processor")
    
    def ram_hdd(self):
        print("Lenovo Laptop RAM & HDD")

class Dell(Laptop):
    
    def ram_hdd(self):
        print("Dell Laptop RAM & HDD")
        
    def processor(self):
        print("Dell Laptop Processor")

# End Users 
print("Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.processor()
lenovo.ram_hdd()    

print("Buying Dell Laptop")
dell = Dell() # TypeError: Can't instantiate abstract class Dell without an implementation for abstract method 'processor'
dell.ram_hdd() 
dell.processor() 

# laptop = Laptop()