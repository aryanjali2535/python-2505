# With Encapsulation & With @property using pythonic way 

class Student:
    def __init__(self,marks):
        self.marks = marks # trigger setter

    # Getter for marks
    @property 
    def marks(self):
        return self.__marks
    
    # Setter for marks
    @marks.setter
    def marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid Marks, only 0-100 allowed")

s1 = Student(90)
print(s1.marks)  # Accessing the getter: 90

# s2 = Student(-10) # ValueError: Invalid Marks, only 0-100 allowed
# print(s2.get_marks())

# updating marks pythonic way 
s1.marks = 95
print(s1.marks)

# updating pythonic way with invalid marks to test
s1.marks = -10
print(s1.marks)

# try:
#     s1.marks = -20  # Attempting to set invalid marks
# except ValueError as e:
#     print(e)  # Output: Price cannot be negative.