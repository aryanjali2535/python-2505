# Trainer Blueprint

from student import Student

class Trainer:
    
    # constructor with instance data 
    def __init__(self, trainer_id, trainer_name):
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        
    # instance method -> display basic trainer info -> hover functionality 
    def trainer_basic_info(self):
        print("=" * 50)
        print("             Basic Trainer Information")
        print(f"Trainer ID: {self.trainer_id}")
        print(f"Trainer Name: {self.trainer_name}")
        print("=" * 50)
        
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
         
        