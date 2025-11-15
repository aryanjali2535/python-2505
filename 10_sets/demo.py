# Sets 

# Empty Set ==> Not set but dict 
empty_set = {}
print(empty_set)
print(type(empty_set))

# Empty Set  
empty_set = set()
print(empty_set)
print(type(empty_set))

# set with numeric data 
num_set = {10,20,30,40,50} 
print(type(num_set))
print(num_set)

# set with text data 
text_set = {"course1","python","course2"}
print(text_set)

# set with mixed data 
mixed_set = {10,20,30,"thirty","student_pass"}
print(mixed_set)

# Duplicates - Not allowed i.e discarded
num_set = {10,20,10,30,40,20,50} 
print(num_set)

# print(dir(num_set))

# Looping data 
num_set = {10,20,10,30,40,20,50} 
for num in num_set:
    print(num)
    

# Frozen Set
num_set = {10,20,10,30,40,20,50} 
print(type(num_set))    

num_fz_set = frozenset({10,20,10,30,40,20,50} )
print(type(num_fz_set))

print(dir(num_fz_set))