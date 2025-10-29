
# Control Structures 

# Indentation
print("Hello")

    # print("Hello") # IndentationError: unexpected indent
    
# using if 
if 5 > 2: # IndentationError: expected an indented block after 'if' statement on line 9
    print("yes thats correct") # at least 1 space 
#  print("let's see how this goes") # IndentationError: unindent does not match any outer indentation level    
    print("let's see how this goes")

# another block
if 10 > 5:
 print("true")  
 
# if statement
# if condition:
#     Statements  
num = 10
if num > 0:
    print(f"Number {num} is positive")

num = -10
if num > 0:
    print(f"Number {num} is positive")
    
num = -10
if num > 0:
    print(f"Number {num} is positive")
else:
    print(f"Number {num} is Negative")
    
age = 22
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote")
    
# input() use case
name = input("Enter Your Name: ")
print("Welcome "+name)

# Vote App
age = int(input("Enter Your Age: ")) # type casting)
# age = int(age)
if age >= 18: # TypeError: '>=' not supported between instances of 'str' and 'int'
    print("You Can Vote")
else:
    print("You Cannot Vote")
    
# Ternary operation
age = int(input("Enter Your Age: ")) # type casting)
# variable = value_if_true if condition else value_if_false 
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)

# elif 
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")   
elif marks >= 35:
    print("E")    
else:
    print("FAILED")
    
# match case 
choice = int(input("Enter Your Choice: "))
match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid")
