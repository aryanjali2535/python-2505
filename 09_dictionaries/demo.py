# Dictionaries

# Empty Dictionary  
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# Empty Dictionary  
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# dictionary with numeric data 
# num_dict = {10,20,30,40,50} 
num_dict = {1:10,2:20,3:30} 
print(type(num_dict))
print(num_dict)

# dictionary with text data 
text_dict = {"course1":"python","course2":"django","course3":"ai"}
print(text_dict)

# dictionary with mixed data 
mixed_dict = {10:20,30:"thirty","student_pass":True}
print(mixed_dict)

# Duplicates - values
num_dict = {1:10,2:20,3:30,4:30,5:30} 
print(type(num_dict))
print(num_dict)

# Duplicates - keys
num_dict = {1:10,2:20,2:20.0,1:0,3:30,1:5} 
print(type(num_dict))
print(num_dict)

# Keys should be immutable objects
# num_dict = {[10]:10,2:20,3:30,4:30,5:30} 
num_dict = {(10):10,2:20,3:30,4:30,5:30} 
print(type(num_dict))
print(num_dict)

# real world dictionary use case - JSON Data 
students = {
    "101": {
        "name": "Ravi",
        "email": "ravi2krishna@gmail.com",
        "courses": ["python","django","ai"],
        "course_prices": (10000,20000,30000) 
    },
    "102": {
        "name": "John",
        "email": "john@yahoo.com",
        "courses": ["java","spring","ai"],
        "course_prices": (15000,25000,35000) 
    }
}

print(type(students))

print(students)

# Access Data 
# print(students[0]) # KeyError: 0
# print(students[101]) # KeyError: 101
print(students["101"])
print(students["101"]["name"])
print(students["101"]["courses"])
print(students["101"]["courses"][1])

# want to do operations -> check user is google customer
id = "102"
if students[id]["email"].endswith("@gmail.com"):
    print("Google Customer")
else:
    print("Not Google Customer")
    
# looping the data 
num_dict = {1:10,2:20,3:30} 
# print(dir(num_dict))
print(num_dict)

print(num_dict[2])

# by default we got access to keys
for num in num_dict:
    print(num)
    
# now access values using keys
for key in num_dict:
    print(num_dict[key])
    
# using operators to manipulate data
for key in num_dict:
    print(num_dict[key] * 10)
    
# dict operations
print(dir(num_dict))