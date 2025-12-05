# No Encapsulation & No Getters & Setters 

class Student:
    def __init__(self,marks):
        self.marks = marks
        
s1 = Student(90)
print(s1.marks)

s1 = Student(-10)
print(s1.marks)