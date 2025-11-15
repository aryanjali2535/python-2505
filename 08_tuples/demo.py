# Tuples 

# empty tuple 
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

# empty tuple 
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))

# tuples with numeric data 
num_tuple = (10,20,30,40,50) # Homogenous 
print(num_tuple)

# num_tuple = tuple(10,20,30,40,50) # TypeError: list expected at most 1 argument, got 5
num_tuple = tuple([10,20,30,40,50])
print(num_tuple)

# tuples with text data 
text_tuple = ("python","django","ai")
print(text_tuple)

# tuple with mixed data 
mixed_tuple = (10,20,30,"python","django","ai",3.5,True) # heterogenous 
print(mixed_tuple)

# Access / Retrieve Data 
num_tuple = (10,20,30,40,50)
first_element = num_tuple[0]
last_element = num_tuple[-1]
print(num_tuple)
print(first_element)
print(last_element)

#  access error
# print(num_tuple[10]) # IndexError: list index out of range

# access range of values 
num_tuple = (10,20,30,40,50)
print(num_tuple[::])
print(num_tuple[1:3:]) # [20, 30]
print(num_tuple[0:5:2]) # [10, 30, 50]

# access individual values using for loop 
for num in num_tuple:
    print(num)
    
# perform some operations on data
for num in num_tuple:
    print(num * 5)
    
# # perform some conditionals 
num_tuple = (10,20,30,40,50)
for num in num_tuple:
    # check for even 
    if num % 2 == 0:
        print(num)

num_tuple = (10,20,35,40,55,60)
for num in num_tuple:
    # check for odd 
    if num % 2 == 1:
        print(num)

# Duplicates 
num_tuple = (10,20,30,40,50,10,20)
print(num_tuple)

# Check functionalities 
print(dir(num_tuple))