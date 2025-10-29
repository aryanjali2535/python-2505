# Solution for 
# Simulate a OTP Verification System / Password / Bank ATM Pin

actual_otp = 1234
attempts = 3
# print(len(str(actual_otp)))
while attempts > 0:
    print(f"You have {attempts} left")
    user_otp = int(input("Enter OTP: "))
    
    # check if the otp is 4 digits 
    if len(str(user_otp)) != 4:
        print("❌ OTP Must be 4 Digits")
        attempts -= 1
        continue 
    
    # check if otp is correct 
    if user_otp == actual_otp:
        print("✅ Correct OTP - Transaction Success")
        break
    else:
        print("❌ Incorrect OTP")
        attempts -= 1
        
else:
    print("🚫 Maximum Attempts Reached, Try after 24 Hours")
     