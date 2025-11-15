# Working With JSON Data / Files 

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","ai"],
    "gpa": 8.5
}

print(type(student))
print(student)

# Writing Dictionary Data As JSON File 
import json
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)

# Writing Dictionary Data As JSON File With Indentation
with open("14_file_manage/stu.json","w") as file_data:
    json.dump(student,file_data,indent=4)

print("=" * 50)

# Reading Data From JSON File
with open("14_file_manage/stu.json","r") as file_data:
    json_reader = json.load(file_data)
print(json_reader)
print(type(json_reader))

# Get Student Name & Number Of Courses 
with open("14_file_manage/stu.json","r") as file_data:
    json_reader = json.load(file_data)
print("Name: ",json_reader["name"])    
print("No Of Courses Enrolled: ",len(json_reader["courses"]))   
    
# Check If Student Passed Or Not Based On GPA is above 7 
with open("14_file_manage/stu.json","r") as file_data:
    json_reader = json.load(file_data)

if json_reader["gpa"] > 7:
    print(f"{json_reader["name"]} Passed ")
else:
    print(f"{json_reader["name"]} Failed ")

# Object Based Rather Then Files (dumps & loads)

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","ai"],
    "gpa": 8.5
}
print(type(student))

data = json.dumps(student)
print(data)
print(type(data))

str_data = '{"id": 101, "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "django", "ai"], "gpa": 8.5}'
print(type(str_data))
data = json.loads(str_data)
print(data)
print(type(data))

print("=" * 20)

# Building Full Stack Application 
import urllib.request

# The URL you want to get data from
url = 'https://dummyjson.com/users'

response = urllib.request.urlopen(url)
print(response)
print(type(response))

# Read the content of the response
data = response.read()
print(data)
print(type(data))

# Convert Data To Python Dictionary 
parsed_data = json.loads(data)
print(parsed_data)
print(type(parsed_data))

# Customer Requirement - List Me Users 
users = parsed_data["users"]
print(users)

# Customer Requirement - List Me Usernames & Number Of Users
# user_names = parsed_data["users"]["username"]
for user in users:
    print(user["username"])
    
print("Number Of Users: ",len(users))

# Customer Requirement - List Me Users With Age Below 30
for user in users:
    if user['age'] < 30:
        print(user["username"], user['age'] )
        