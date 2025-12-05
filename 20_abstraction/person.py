from contracts import Personable

# Parent Class Will Abstract Class, With Common Attributes For ALl Persons 
class AbstractPerson(Personable):
    # constructor with instance data 
    def __init__(self, id=None, name=None, age=None, email=None, mobile_number=None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.mobile_number = mobile_number
    
    # For Encapsulation Implementing setters & getters Using @property decorator 
    # id
    @property
    def id(self):
        return self.__id 
    
    @id.setter
    def id(self,value):
        self.__id = value
        
    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
    
    # email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    # mobile_number 
    @property
    def mobile_number(self):
        return self.__mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self.__mobile_number = value
        
    # implement contract -> set_person_details
    def set_person_details(self,id, name, age, email, mobile_number):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.mobile_number = mobile_number
        
    # implement contract -> person_complete_info
    def person_complete_info(self):
        print("=" * 50)
        print("             Complete Information")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Mobile: {self.mobile_number}")
        print("=" * 50)