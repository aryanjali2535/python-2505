# Vote App
age = int(input("Enter Your Age: ")) # type casting
if age >= 18: 
    has_id = input("Do You Have id (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Need an id to vote") 
else:
    print("You Cannot Vote")

# Nested Loops
# Math Table 
# nested for loop
for outer in range(1,5):
    for inner in range(1,5):
        print(f"{outer} * {inner} = {outer*inner}")
    print("==========")

# nested while loop 
row = 1   
while row < 6:
    column = 1
    while column < 6:
        print(f"{row} * {column} = {row*column}")
        column+=1
    print("==========")
    row+=1
    
# Ecommerce App
carts = [
    [("Apple", 30), ("Banana", 10), ("Orange", 20)],       # Cart 1
    [("Milk", 50), ("Bread", 25)],                         # Cart 2
    [("Shampoo", 120), ("Soap", 40), ("Toothpaste", 60)]   # Cart 3
]