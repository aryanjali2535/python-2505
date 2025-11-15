# List Related Operations

# append() : adds an element to the end of the list
data = [10,20,30,40,50]
print("Original: ",data)
# data.append() # TypeError: list.append() takes exactly one argument (0 given)
data.append(60)
print("Updated: ",data)

products = ["laptop","iphone","ipad"]
print(products)

# add new product 
products.append("pc")
print(products)

data = [10,20,30,40,50]
# data.append(60,70,80) # TypeError: list.append() takes exactly one argument (3 given)
data.append([60,70,80])
print(data) # [10, 20, 30, 40, 50, [60, 70, 80]]

# extend() : adds an iterable to the end of the list
data = [10,20,30,40,50]
print(data)
# data.extend() # TypeError: list.extend() takes exactly one argument (0 given)
# data.extend(60) # TypeError: 'int' object is not iterable
data.extend([60])
print(data)

data = [10,20,30,40,50]
print(data)
data.extend([60,70,80])
print(data)

# insert() : insert data at specific position (index)
data = [10,20,40,50]
print(data)

# data.insert(30) # TypeError: insert expected 2 arguments, got 1
data.insert(2,30)
print(data)

data.insert(10,100) # if you give index out of range, element is added at the end
print(data)

# Lists are mutable 
data = [10,20,34,40,50]
print(data)
data[2] = 30 
print(data)

# pop() : remove last item in the list by default, or based on index also we can remove
data = [10,20,30,40,50]
print(data)

data.pop() # by default last element 
print(data)

data.pop(0) # based on index also you can delete 
print(data)

# data.pop(10) # IndexError: pop index out of range
# print(data)

removed_element = data.pop(0) # based on index also you can delete 
print(removed_element)
print(data)

# remove() : remove element based on value 
data = [10,20,30,40,50]
print(data)
data.remove(30) # not index, it's value now 
print(data)

# data.remove(300) # ValueError: list.remove(x): x not in list
# print(data)

data = [10,20,30,40,50,10,60,10,70]
print(data)
data.remove(10) # not index, it's value now 
print(data)

# Remove all occurrences of 10
data = [10,20,30,40,50,10,60,10,70]
print(data)
data.remove(10) # not index, it's value now 
print(data)

# logic to remove all occurrences
data = [10,20,30,40,50,10,60,10,70]
print(data)

while 10 in data:
    data.remove(10)
print(data)

# clear() : removes all elements and empties list 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index() : used to get the index position of value
data = [10,20,30,40,50]
print(data)
print(data.index(40))
print(data.index(10))
# print(data.index(100)) # ValueError: 100 is not in list

# count() : used to count the number of occurrences of a value
data = [10,20,30,40,50,10,60,10,70]
print(data)

print(data.count(10))
print(data.count(100))

# reverse() : reverse the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort() : sort the list, default is ascending order
data = [40,20,30,10,50]
print(data)
data.sort()
print(data)
data.sort(reverse=True) # descending order
print(data)

data = ["a","d","b"]
print(data)
data.sort()
print(data)

data = ["a",0,"d","b",3]
print(data)
# data.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
print(data)

# copy() : create a backup copy
data = [10,20,30,40,50]
print(data)
data_backup =  data.copy()
print(data_backup)