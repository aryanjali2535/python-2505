# laptop contract (Govt said these are must for building laptops)

# Without Abstraction (No Abstract Classes)

# Concrete Class
class Laptop:
    
    # concrete methods 
    def processor(self):
        print("Laptop Processor")
    
    def ram_hdd(self):
        print("Laptop RAM & HDD")

# Implementations -> Laptop Manufactures 
class Lenovo(Laptop):
    
    def processor(self):
        print("Lenovo Laptop Processor")
    
    def ram_hdd(self):
        print("Lenovo Laptop RAM & HDD")
        
class Dell(Laptop):
    
    def ram_hdd(self):
        print("Dell Laptop RAM & HDD")
    
# End Users 
print("Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.processor()
lenovo.ram_hdd()

print("Buying Dell Laptop")
dell = Dell()
dell.ram_hdd()