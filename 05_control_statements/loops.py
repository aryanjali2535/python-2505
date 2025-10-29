
# Loops - Repetition 

# while loop 
    # You can use while loop, when you don't know 
    # number of iterations in advance 

# Password Auth 
password = "1234"
user_given_password = ""

while user_given_password != password:
    user_given_password = input("Enter Password: ")
    
print("Password Matched, Login Success")

# for loop 
# iterate over a sequence
# when you know number of iterations in advance 
just_num = 10
print(just_num)

list_numbers = [10,20,30,40,50]
for num in list_numbers:
    print(num)
    
some_string = "python"
for char in some_string:
    print(char)
    # print(char,end=",")
    
number = "1001" # TypeError: 'int' object is not iterable
# print(dir(number))

# for num in number:
#     print(num)

# another use-case with for is automation 
print("Hi")

# Say Hi 10 times
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi") 
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

# Range 
for num in range(10):
    print(num)
    
for num in range(10):
    print("Hi")
    
for num in range(2,10,1):
    print(num)    
    
for num in range(2,10,2):
    print(num)    
