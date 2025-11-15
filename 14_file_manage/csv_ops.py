# Working With CSV files 

import csv

# Read Data 
with open("14_file_manage/students.csv","r") as file_data:
    # print(file_data)
    csv_reader = csv.reader(file_data)
    # print(csv_reader)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Assume we have 10k records like this 
# Customer Requirement : Fetch me details of Hyderabad customers 
filter_by_city = "Hyderabad"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[3] == filter_by_city:
            print(row)

print("=" * 50)

# Assume we have 10k records like this 
# Customer Requirement : Fetch me details of gmail customers 
filter_by_email = "@gmail.com"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[1].endswith(filter_by_email):
            print(row)

print("=" * 50)
            
# As per some new business requirements we changed the structure of data set 
# Customer Requirement : Fetch me details of gmail customers 
filter_by_email = "@gmail.com"
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[2].endswith(filter_by_email):
            print(row)

print("=" * 50)
            
# Now working with dynamic data sets not relying on fixed index 
filter_by_email = "@gmail.com"
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row["email"].endswith(filter_by_email):
            print(row)

print("=" * 50)
            
filter_by_email = "@gmail.com"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row["email"].endswith(filter_by_email):
            print(row)
        
# Writing Data To CSV Files Overwrite Mode
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(["name","email","mobile","address"])
    csv_writer.writerow(['Kishore', 'kishore296@gmail.com', '9642197818', 'Jaipur'])
    csv_writer.writerows([['Ravi', 'ravi624@gmail.com', '9693547237', 'Coimbatore'],
                        ['Naveen', 'naveen959@gmail.com', '9956567915', 'Bangalore'],
                        ['Vijay', 'vijay947@gmail.com', '9596374936', 'Coimbatore']])

# Writing Data To CSV Files Append Mode
with open("14_file_manage/test.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(["name","email","mobile","address"])
    csv_writer.writerow(['Kishore', 'kishore296@gmail.com', '9642197818', 'Jaipur'])
    csv_writer.writerows([['Ravi', 'ravi624@gmail.com', '9693547237', 'Coimbatore'],
                        ['Naveen', 'naveen959@gmail.com', '9956567915', 'Bangalore'],
                        ['Vijay', 'vijay947@gmail.com', '9596374936', 'Coimbatore']])    


# Writing Data To CSV Files Using Dict Writer
# with open("14_file_manage/new.csv","w") as file_data: # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
fieldnames = ["name","email","mobile","address"]
with open("14_file_manage/new.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames)
    # csv_writer.writerow({'name': 'Kishore', 'email': 'kishore309@gmail.com', 'mobile': '9835847972', 'address': 'Pune'}) # only rows no fields for columns 
    csv_writer.writeheader() # to write the fieldnames as the first row in the CSV file.
    csv_writer.writerow({'name': 'Kishore', 'email': 'kishore309@gmail.com', 'mobile': '9835847972', 'address': 'Pune'}) 
    csv_writer.writerow({'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'})
    csv_writer.writerows([{'name': 'Ajay', 'email': 'ajay280@gmail.com', 'mobile': '9205777629', 'address': 'Mumbai'},
                        {'name': 'Ravi', 'email': 'ravi624@gmail.com', 'mobile': '9693547237', 'address': 'Coimbatore'},
                        {'name': 'Naveen', 'email': 'naveen959@gmail.com', 'mobile': '9956567915', 'address': 'Bangalore'}])


# Writing Data To CSV Files Append Mode
with open("14_file_manage/demo.csv","a") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader() # to write the fieldnames as the first row in the CSV file.
    csv_writer.writerow({'name': 'Kishore', 'email': 'kishore309@gmail.com', 'mobile': '9835847972', 'address': 'Pune'}) 
    csv_writer.writerow({'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'})
    csv_writer.writerows([{'name': 'Ajay', 'email': 'ajay280@gmail.com', 'mobile': '9205777629', 'address': 'Mumbai'},
                        {'name': 'Ravi', 'email': 'ravi624@gmail.com', 'mobile': '9693547237', 'address': 'Coimbatore'},
                        {'name': 'Naveen', 'email': 'naveen959@gmail.com', 'mobile': '9956567915', 'address': 'Bangalore'}])