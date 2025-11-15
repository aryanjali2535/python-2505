# Strings 

# define single line strings 

# single quote
s1 = 'hello'
print(s1)

# double quote
s2 = "hello"
print(s2)

# triple quote
s3 = """hello"""
s4 = '''hello'''
print(s3)
print(s4)

# define multi line strings 

# address = "house no 90
# zip 500081
# city hyderabad
# state telangana
# country india"

address = """house no 90
zip 500081
city hyderabad
state telangana
country india"""

print(address)

address = '''house no 90
zip 500081
city hyderabad
state telangana
country india'''

print(address)

# need single quote in a string -> double quotes (" ")
question = "how are you ?"
# answer = 'i'm fine' # SyntaxError
answer = "i'm fine"
print(answer)

# need double quote in a string -> single quotes (' ')
question = "how are you ?"
# answer = "i"m fine" # SyntaxError
answer = 'i"m fine'
print(answer)

# need both single & double quotes -> triple quotes (''' ''')
question = "how are you ?"
# answer = " i"m fine i'm fine " # SyntaxError
answer = '''i"m fine i'm fine '''
print(answer)

# Access String 
text = "python"
print(text)

# Access Characters Using Index 
print(text[2]) # positive index 
print(text[-1]) # negative index 

# print(text[10]) # IndexError: string index out of range

# Access all characters 
text = "python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# using loops with string 
text = "python"

for char in text:
    print(char)
    
# len() will return number of items in a object which can be used with string 
text = "python"
print("Number Of Characters: ",len(text))

# slicing positive 
text = "python"
print(text[0:5:1])
print(text[0:3:1])
print(text[1:3])
print(text[0:5:2])
print(text[:])
print(text[::])

#                0   1   2   3   4   5 (Positive Indexing) (Left To Right) (---->)
#                 p   y   t   h   o   n
#                 -6  -5  -4  -3  -2  -1 (Negative Indexing) (Right To Left) (<----)

# slicing negative
text = "python"
print(text[-4:-1])
print(text[-4:-1:1])
print(text[-4:-1:-1]) # empty 
print(text[-4:-6:1]) # empty 
print(text[-4:-7:-1]) # ty

print(text[::])
print(text[::-1])

# with logic
text = "python"
reversed_text = "" # typ

for char in text:
    reversed_text = char + reversed_text # 
print(reversed_text)

# String Concatenation 
s = "good"
m = " morning"
print(s+m)

# Formatted String Literals - interpolation
age = 30
# print("My age is: "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My age is: {age}")

laugh = "HaHa"
print(laugh)

# String Repetition 
hard_laugh = laugh * 20
print(hard_laugh)

# String Immutability 
greet = "hello" 
print(greet) # -> Hello
print(greet[0])
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet[0])
print(type(greet))

print(dir(greet))