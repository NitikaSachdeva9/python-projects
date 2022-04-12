#This program validates the email address provided by the user by using regex to check the conditions.
#Conditions - 
#1. Check all the chars are lower case
#2. Check all the chars are a-z, 0-9
#3. '.' and '_' can occur once in the string
#4. '@' can occur once in the string
#5. 2,3 char from the back should be a '.'
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('Enter your Email Address: ')
if re.search(email_condition, user_email):
    print("Congratulations, Your email address satisfy all the conditions.")
else:
    print("Your email address is not as per the standards.")
