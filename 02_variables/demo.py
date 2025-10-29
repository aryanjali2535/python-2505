# Working With Variables 

# Assign Data
# variable_name = value 
student_name = "Ravi" # string 
student_age = 25 # int
student_gpa = 9.5 # float
student_passed = True # boolean

# Retrieve Data 
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)

# Get Identity/Memory Address Of Variables 
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))

# Get Data Type
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))

# Variables can change during the execution dynamically 
dynamic_data = 10 
print(type(dynamic_data))

dynamic_data = "10" 
print(type(dynamic_data))

dynamic_data = 10.0
print(type(dynamic_data))

# Memory Model Of Python 
value_x = 10
print(id(value_x))

value_y = 20
print(id(value_y))

value_z = 10
print(id(value_z))


value_list_x = [10,20,30,40,50]
print(id(value_list_x))

value_list_y = [10,20,30,40,50] # -> 0 = 10, 1 = 20, 2 = 30 .....
print(id(value_list_y))

print(id(value_list_x[0]))
print(id(value_list_y[0]))
print(id(value_x))
print(id(value_z))

# Variables 
student_name = "Ravi" # string 
student_age = 25 # int
student_gpa = 9.5 # float
student_passed = True # boolean

# Retrieve Data 
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)

# Concatenation
x = "Python "
y = "is "
z = "easy"

# print(xyz) # NameError: name 'xyz' is not defined
print(x + y + z)

a = 10
b = 20
c = 30

print(a + b + c)

# print(a+x) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Profile 
name = "Ravi"
age = 25
print("My Name is "+name)
# print("My Age is "+25) # TypeError: can only concatenate str (not "int") to str

# My Name is Ravi and my age is 25
print("My Name is "+name + " and my age is",age  )
print("My Name is ",name + " and my age is",age  )

print("My Name is "+name + " and my age after 5 years would be",age+5  )
# print("My Name is "+name + " and my age after 5 years would be"+age+5  )


a = 10
b = 20
c = 30

a,b,c = 10,20,30 # Valid ==> Always LHS == RHS 
print(a+b+c)

# a,b,c = 10,20,30,40 # ValueError: too many values to unpack (expected 3)
print(a+b+c)

a = 10
b = 20
c = 10
d = 10

a = c = d = 10
print(a)
print(c)
print(d)

# Profile 
name = "Ravi"
age = 25

#  -> without interpolation (till python 2)
print("My Name is "+name + " and my age is",age  )
print("My Name is ",name + " and my age is",age  )

print("My Name is "+name + " and my age after 5 years would be",age+5  )


# With interpolation
print("My Name is {name} and my age is {age}")
print(f"My Name is {name} and my age is {age}")
print(f"My Name is {name} and my age is {age+5}")