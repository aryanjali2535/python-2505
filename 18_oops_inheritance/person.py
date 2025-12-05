# Parent Class With Common Attributes For ALl Persons 
class Person:
    # constructor with instance data 
    def __init__(self, id=None, name=None, age=None, email=None, mobile_number=None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.mobile_number = mobile_number
    
    # common method for all persons 
    def person_complete_info(self):
        print("=" * 50)
        print("             Complete Information")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Mobile: {self.mobile_number}")
        print("=" * 50)