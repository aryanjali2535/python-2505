
# Branching Statements 

# loop without break
for num in range(1,11):
    print(num)
print("=======")    

# loop with break
for num in range(1,11):
    if num == 5:
        break # stop from 5
    print(num)
print("=======")   

# loop with continue
for num in range(1,11):
    if num == 5:
        continue # skip 5
    print(num)
print("=======")  

# using pass 
emp_sal = 25000

# requirement to perform some future operation 
# if emp salary is 25000 or above
if emp_sal >= 25000:
    pass # acts as a placeholder for my future code

# new functionality which i know 
print("New Functionality Completed")
