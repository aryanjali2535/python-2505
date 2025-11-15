# String Methods / Operations 

# Simulate Gmail Functionality 
# RaVI2KRIshna -> ravi2krishna@gmail.com 
# strip used in gmail -> leading and trailing whitespace removed
email = input('Enter Your Email ID: ')
format_email = email.lower().strip()
print("Original Email: "+email)
print("Formatted Email: "+format_email)
print("Formatted Email: "+format_email+"@gmail.com")

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input('Enter Your PAN ID: ')
# print(pan.isalnum())
if pan.isalnum():
    format_pan = pan.upper()
    print("Original PAN: "+pan)
    print("Formatted PAN: "+format_pan)
else:
    print("PAN Id is Invalid")

# Phone ISD Scenario
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png

mobile_number = input('Enter Phone Number with ISD CODE: ')

if mobile_number.startswith("+91"):
    print("Calling India Number Charged In Rupees")
elif mobile_number.startswith("+1"):
    print("Calling USA Number Charged In Dollars")
elif mobile_number.startswith("+33"):
    print("Calling France Number Charged In Euros")
else:
    print("Calling Supported To Only India, USA & France Numbers")
    
# Email Synchronization
source_email = input('Enter Your Source Email ID: ')
dest_email = input('Enter Your Destination Email ID: ')

if source_email.endswith("@gmail.com") and dest_email.endswith("@gmail.com"):
    print("Email Synchronization Started")
else:
    print("Email Synchronization Failed, Both should be same providers")
    

# Simulate CSV data (comma separated values)
# Name, Email, Age, City, Job_Role
emp_john_data = "John,john@gmail.com,25,Hyderabad,Developer"
print(emp_john_data)
# Display Only Users Name & Job Role
print("Name: "+emp_john_data[0])
print("Job Role: "+emp_john_data[-1])

# Using String techniques -> split() default break is space
list_data = emp_john_data.split()
print(list_data)
fields = emp_john_data.split(",")
print(fields)

print("Name: "+fields[0])
print("Job Role: "+fields[-1])

# Amazon Order Email Confirmation
order_template_amazon = "Hello User, your order with {order_id} has been shipped"

order_ids = "AMZ-IN-89898987,AMZ-IN-756765887,AMZ-IN-90997987"

order_list = order_ids.split(",")

for order_id in order_list:
    user_email = order_template_amazon.replace("{order_id}",order_id)
    print(user_email)