# Data Types

# Numeric Types 
data = 10
print(type(data))
data = -10
print(type(data))

data = 10.0
print(type(data))

# data = 3+i5
j = 10
data = 3+5j
print(type(data)) 

# Text data 
data = "good morning"
print(type(data)) 

# Boolean Data
data = True
print(type(data)) 

# None Type 
data = None
print(type(data)) 

# List Type
data = [10,20,30,40,50]
print(type(data)) 

# Tuple Type
data = (10,20,30,40,50)
print(type(data)) 

# Set Type
data = {10,20,30,40,50}
print(type(data)) 

# Dictionary Type
data = {"name":"name is used to identify some entity","age":"represents how old an entity is"}
data = {"name":"ravi","age":25}
print(type(data)) 

# Custom Data Type
class Student:
    pass 

data = Student()
print(type(data))

# Data 
n1 = 10 # int
n2 = 5.5 # float 

sum = n1 + n2 
print(sum) # 15.5 
print(type(sum)) # 15.5 

# Value 
pi = 3.14 # float 
print(type(pi))
# my req is convert to integer
pi_int = int(pi)
print(pi_int)
print(type(pi_int))

# some user in web app gave some rating (string)
rating = "4"
print(type(rating))

# now requirement is increment rating by 1 
# type casting
rating = int(rating)
rating = rating + 1 # TypeError: can only concatenate str (not "int") to str
print(rating)
print(type(rating))

int = 4
str_int = str(int)
print(type(str_int))