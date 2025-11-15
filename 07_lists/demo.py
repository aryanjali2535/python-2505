# Lists 

# empty list 
empty_list = []
print(empty_list)
print(type(empty_list))

# empty list 
empty_list = list()
print(empty_list)
print(type(empty_list))

# list with numeric data 
num_list = [10,20,30,40,50] # Homogenous 
print(num_list)

# num_list = list(10,20,30,40,50) # TypeError: list expected at most 1 argument, got 5
num_list = list([10,20,30,40,50])
print(num_list)

# list with text data 
text_list = ["python","django","ai"]
print(text_list)

# list with mixed data 
mixed_list = [10,20,30,"python","django","ai",3.5,True] # heterogenous 
print(mixed_list)

# Access / Retrieve Data 
num_list = [10,20,30,40,50]
first_element = num_list[0]
last_element = num_list[-1]
print(num_list)
print(first_element)
print(last_element)

# access error
# print(num_list[10]) # IndexError: list index out of range

# access range of values 
num_list = [10,20,30,40,50]
print(num_list[::])
print(num_list[1:3:]) # [20, 30]
print(num_list[0:5:2]) # [10, 30, 50]

# access individual values using for loop 
for num in num_list:
    print(num)
    
# perform some operations on data
for num in num_list:
    print(num * 5)
    
# perform some conditionals 
num_list = [10,20,35,40,55,60]
for num in num_list:
    # check for even 
    if num % 2 == 0:
        print(num)

num_list = [10,20,35,40,55,60]
for num in num_list:
    # check for odd 
    if num % 2 == 1:
        print(num)

# Duplicates 
num_list = [10,20,30,40,50,10,20]
print(num_list)

# Check functionalities 
print(dir(num_list))