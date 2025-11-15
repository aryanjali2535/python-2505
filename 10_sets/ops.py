# Set Operations 

# add() : adds an element to the set
data = {10,20,30,40,50}
print("Original: ",data)
data.add(60)
print("Updated: ",data)

# update(): adds multiple elements(iterables)
data = {10,20,30,40,50}
print("Original: ",data)
data.update([60,70,80])
print("Updated: ",data)

# remove(): remove element from set set if found, if not found we get error 
data = {10,20,30,40,50}
print("Original: ",data)
data.remove(10)
print("Updated: ",data)

# data.remove(100) # KeyError: 100
# print("Updated: ",data)

# discard(): remove element from set if found, if not found no error 
data = {10,20,30,40,50}
print("Original: ",data)
data.discard(10)
print("Updated: ",data)
data.discard(100) 
print("Updated: ",data)

# clear(): removes and empties the set
data = {10,20,30,40,50}
print("Original: ",data)
data.clear()
print("Updated: ",data)

# copy(): makes a copy
data = {10,20,30,40,50}
print("Original: ",data)
backup = data.copy()
print("Backup: ",backup)

# set specific operations 

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): combine both sets 
print(s1.union(s2))
print(s1 | s2) # pipe symbol

# intersection(): extract common elements from both sets 
print(s1.intersection(s2))
print(s1 & s2) # ampersand symbol
print(s1)
print(s2)

# intersection_update(): extract common elements from both sets, also update calling set 
print(s1.intersection_update(s2))
# print(s2.intersection_update(s1))
print(s1)
print(s2)

# difference(): remove common and give unique elements from calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1 - s2)
print(s1)
print(s2)

# difference_update(): remove common and give unique elements from calling set, also update calling set  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference(): removes common elements and takes combined elements from both sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2) # cap symbol

# symmetric_difference_update(): removes common elements and takes combined elements from both sets, also update calling set  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1)
print(s2)
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): checks if the given set is subset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}
print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): checks if the given set is superset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}
print(s1.issuperset(s2))
print(s1.issuperset(s3))

# isdisjoint(): checks if the sets have no common elements
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

print(dir(s1))