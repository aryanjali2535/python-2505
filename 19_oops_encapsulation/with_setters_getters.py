# With Encapsulation & With Getters & Setters 

class Student:
    def __init__(self,marks):
        self.set_marks(marks) # Validation applied at object creation
    
    # getter 
    def get_marks(self):
        return self.__marks 

    # setter 
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid Marks, only 0-100 allowed")
        
s1 = Student(90)
# print(s1.marks) # AttributeError: 'Student' object has no attribute 'marks'
# With Above We can say, you cannot directly change object state

# Now let's add getter method to get data 
print(s1.get_marks()) 

# Now let's add invalid marks like 
s2 = Student(-10)
print(s2.get_marks()) # this is not correct right, -10 cannot be marks

# For above issue, we got setter methods where we can do validations
s3 = Student(-20)
print(s3.get_marks())

# This is more of java / c++ way of implementation 

# Python provides its own way of above implementation
#    using @property Decorator: This decorator allows you to define methods 
#    that can be accessed like attributes, providing a "Pythonic" way 
#    to implement getters, setters