# contract for person details, entities like persons like student, trainer etc 
# contract for payment details, entities like persons like student, trainer etc 

# With Abstraction (With Abstract Classes)

from abc import ABC, abstractmethod

# contract for person details
class Personable(ABC):
    
    # Set Person Details for Entity
    @abstractmethod
    def set_person_details(self,id, name, age, email, mobile_number):
        pass 
    
    # Display Person Details for Entity
    @abstractmethod
    def person_complete_info(self):
        pass

# contract for payment details
class Payables(ABC):    
    # Contract for entities involved in payment calculations 
    @abstractmethod
    def calculate_payment(self):
        pass