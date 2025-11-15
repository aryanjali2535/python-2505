# Dictionary methods 

data = {"a":"apple","b":"banana"} 
print(data)

# update() : add / update item 
# if key exists update, if key doesn't exists add
data.update({"c":"cherry"})
print(data)

data.update({"a":"apricot"})
print(data)

# pop() : removes an item by key
data = {"a":"apple","b":"banana"} 
# data.pop() # TypeError: pop expected at least 1 argument, got 0
data.pop("a")
print(data)
# data.pop("c") # KeyError: 'c'
print(data)

# popitem() : removes last item
data = {"a":"apple","b":"banana"} 
print(data)
data.popitem()
print(data)

# clear() : removes all items, empties dict
data = {"a":"apple","b":"banana"} 
print(data)
data.clear()
print(data)

# get() : used to get the value for a key, if key doesn't exist returns None
data = {"a":"apple","b":"banana"} 
print(data)
# data.get() # TypeError: get expected at least 1 argument, got 0
print(data.get("a"))
print(data.get("c"))

# keys(): used to get keys
data = {"a":"apple","b":"banana"} 
print(data)
print(data.keys())
keys = data.keys()
for key in keys:
    print(key)

# values(): used to get values
data = {"a":"apple","b":"banana"} 
print(data)
print(data.values())
values = data.values()
for value in values:
    print(value)

# items(): gets both keys and values
data = {"a":"apple","b":"banana"} 
print(data)
print(data.items())
data = data.items()
for item in data:
    print(item)
    print(item[0])

# copy() : create a copy of dictionary 
data = {"a":"apple","b":"banana"} 
print(data)
backup = data.copy()
print(backup)

# setdefault() : returns value of a key if present, if not present then sets 
data = {"a":"apple","b":"banana"} 
print(data)
# data.setdefault() # TypeError: setdefault expected at least 1 argument, got 0
out = data.setdefault("b","blueberry")
print(data)
print(out)

data = {"a":"apple","b":"banana"} 
print(data)
out = data.setdefault("c","cherry")
print(data)
print(out)