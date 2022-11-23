#Rajendran Praveen, A20519023

sid = input("Enter your student id: ")

unlock_code = sid[-5:] + "1"
lock_code = sid[-5:] + "4"

print("Enter the string: ")
user_input = input()

for i in range(len(user_input)):
   if user_input[i] == unlock_code[-1]:
       print("Unlocked")
       break
   elif user_input[i] == lock_code[-1]:
       print("Locked")
       break

import re

def security_engine(input_string, access_code):
 if re.search(access_code, input_string):
   print("unlocked")
 else:
   print("locked")

security_engine(user_input, sid)
