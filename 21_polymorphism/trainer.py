# Trainer Blueprint With Person Features
from contracts import Personable
from person import AbstractPerson
from contracts import Payables
from student import Student

class Trainer(Personable, Payables):
    
   # constructor with instance data 
    def __init__(self, trainer_id=None, trainer_name=None, trainer_age=None, trainer_email=None, trainer_mobile_number=None):
        # Using Parent class constructor 
        AbstractPerson.__init__(self,id=trainer_id,name=trainer_name,age=trainer_age,email=trainer_email,mobile_number=trainer_mobile_number)
        
    # instance method -> trainer payment calculation
    def trainer_payment_cal(self):
        total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 2000
        payment_for_sessions = total_sessions_taken * base_pay_per_session
        
        # get student rating 
        print("========= Student Rating Assigned =========")
        # bonus = trainer_rating_calculate()
        student = Student()
        bonus = student.trainer_rating_calculate()
        payment_for_sessions += bonus
        print("========= Trainer Payment To Be Made =========")
        print(f"Total Amount To Be Paid: {payment_for_sessions}")
    
    # implement person info 
    # method override 
    def person_complete_info(self):
        return self.person_complete_info
    
    # method override 
    def set_person_details(self):
        return self.set_person_details()
    
    # implement payments
    # method override  
    def calculate_payment(self):
        return self.trainer_payment_cal()
         
        