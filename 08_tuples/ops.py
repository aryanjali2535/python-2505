# Tuple Related Operations

# Tuple are Immutable 
data = (10,20,34,40,50)
print(data)
# data[2] = 30 # TypeError: 'tuple' object does not support item assignment
print(data)


# index() : used to get the index position of value
data = (10,20,30,40,50)
print(data)
print(data.index(40))
print(data.index(10))
# print(data.index(100)) # ValueError: 100 is not in list

# count() : used to count the number of occurrences of a value
data = (10,20,30,40,50,10,60,10,70)
print(data)

print(data.count(10))
print(data.count(100))