# Create a Python program to calculate the tuition fee discount 
#for students based on their grade levels and academic performance
student_name =input("Enter student name:")
student_grade_level = int(input("Enter student grade level(1-12):"))
base_fee =float(input("Enter Base tuition fee :"))
academic_topper = input("Enter academic_topper(yes/no):")

if student_grade_level<1 or student_grade_level > 12:
    print("Invalid grade level entered. Discount calculation cannot proceed.")
    exit()
discount_rate = 0.0
additional_discount = 0.0

if 9 <= student_grade_level  <= 12:
    if academic_topper == "yes":
        discount_rate = 0.20  # 20% discount
    else:
        discount_rate = 0.10  # 10% discount
elif 6 <= student_grade_level <= 8:
    discount_rate = 0.05  # 5% discount
else:
# Grades below 6
    discount_rate = 0.00  # No discount

if student_grade_level == 10:
    additional_discount = 0.03  # +3% for grade 10
elif student_grade_level == 12:
    additional_discount = 0.05

total_discount =  discount_rate + additional_discount

# Calculate discount amount
discount_amount_saved = base_fee * total_discount
    
# Calculate final fee
final_tuition_fee = base_fee - discount_amount_saved

#summary
print(f"Student Name:{student_name}")
print(f"Grade Level:{student_grade_level}")
print(f"Academic Topper Status:{academic_topper}")
print("-" * 40)
print(f"Base Tuition Fee: {base_fee:,.2f}")
print(f"Total Discount:{total_discount * 100:,.1f}")
print(f"Discount Amount Saved:{discount_amount_saved:,.2f}")
print("-" * 40)
print(f"Final Tuition Fee:{final_tuition_fee:,.2f}")