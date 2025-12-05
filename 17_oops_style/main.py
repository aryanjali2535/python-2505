# Main Logic Calling 

from student import Student
from trainer import Trainer

def main():
    
    # For Student Hovering Functionality
    s1 = Student(101,"John")
    
    # For Student Click Functionality
    s2 = Student(102,"Mike",20,"mike@gmail.com",990909090)
    
    # Calling institute info 
    Student.institute_info()
    
    # Calling Student Basic Info
    s1.student_basic_info()
    
    # Calling Student Complete Info
    s2.student_complete_info()
    
    # Calling Student Calculations Functionality
    s2.achievement_status()
    
    # Calling Student Course Fee Calculations Functionality
    s2.course_fee_cal()
    
    # For Trainer Hovering Functionality
    t1 = Trainer(200,"Ravi")
    
    # Calling Trainer Basic Info
    t1.trainer_basic_info()
    
    # Calling Trainer Payment Functionality
    t1.trainer_payment_cal()

main()
