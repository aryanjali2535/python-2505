
# Operators in python 

# Arithmetic Operators 
num1 = 10
num2 = 5

print(f"Sum of {num1} and {num2} is {num1+num2}")
print(f"Difference of {num1} and {num2} is {num1-num2}")
print(f"Product of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"Modulus of {num1} and {num2} is {num1%num2}")

num1 = 3
num2 = 2

# Floor Division
print(f"Normal Division of {num1} and {num2} is {num1/num2}")
print(f"Floor Division of {num1} and {num2} is {num1//num2}")

# Exponentiation
print(f"Exponentiation Division of {num1} and {num2} is {num1**num2}")


# Compound Assignment Operators
num = 10
# Without Compound Assignment Operators
num = num + 5 
print(num)

num = 10
# With Compound Assignment Operators
num += 5 
print(num)

# increment 
count = 1
# count++ 
count += 1
print(count)

# decrement 
count = 10
# count++ 
count -= 1
print(count)

# Comparison Operators
num1 = 10
num2 = 5
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)

# Logical Operators
num1 = 10
num2 = 5
num3 = 3
num4 = 15
print("==============")
result_and = num1 > num2 and num3 < num4 # T and T -> T
print(result_and)
result_and = num1 < num2 and num3 < num4 # F and T -> F
print(result_and)
print("==============")
result_or = num1 > num2 or num3 < num4 # T or T -> T
print(result_or)

result_or = num1 < num2 or num3 < num4 # F or T -> T
print(result_or)

result_or = num1 < num2 or num3 > num4 # F or F -> F
print(result_or)

print("==============")

result_not = num1 < num2 or num3 > num4 # F or F -> F
print(result_not)
print(not result_not)

print("==============")

# Membership Operators
data = "python is easy to learn"
find_word = "java"
found = find_word in data
print(found)

data = "python is easy to learn"
find_word = "python"
found = find_word in data
print(found)


# Employees -> 10
employee_ids = [101,102,103,104,105,106,107,108,109,110]
find_emp = 125
found = find_emp in employee_ids
print(found)

# Employees -> 10
employee_ids = [101,102,103,104,105,106,107,108,109,110]
find_emp = 125
found = find_emp not in employee_ids
print(found)

# data = 1001
# find_word = 0
# found = find_word in data # TypeError: argument of type 'int' is not iterable
# print(found)

data = "1001"
# print(dir(data)) # __iter__

# Identity Operators
n1 = 10
n2 = 10

print(n1 is n2)
print(n1 == n2)

n1 = 10
n2 = 10.0

print(n1 is n2)
print(n1 == n2)

# Bitwise Operators
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111
       # 0000000000000001

print(n1 & n2)
print(n1 | n2)

# Calculate EMI for a acr 
on_road_price = 2000000
down_payment = 500000
interest_rate = 9.5
loan_period_years = 4 

# calculations
loan_amount = on_road_price - down_payment
months = loan_period_years * 12
monthly_interest_rate = interest_rate / (12*100)

# EMI Calculation 
# EMI = [P x R x (1+R)^N] / [(1+R)^N – 1]
emi = (loan_amount*monthly_interest_rate*(1+monthly_interest_rate) ** months) / (((1+monthly_interest_rate) ** months) - 1)

payable_amount = emi * months

print(emi)
print(payable_amount)
