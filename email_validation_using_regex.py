#This program validates the email address provided by the user by using regex to check the conditions.
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('Enter your Email Address: ')
if re.search(email_condition, user_email):
    print("Congratulations, Your email address satisfy all the conditions.")
else:
    print("Your email address is not as per the standards.")
