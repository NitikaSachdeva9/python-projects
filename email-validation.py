#This program takes email address as input from the user and runs 5 constraints to validate if the email address is as per the standards
email=input("Enter your email address:")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Condition:5 | Email address cannot have a space, upper char. Can have digit, _ , . , @")
                else:
                    print "Bingo, the Email Address is as per the standards"
            else:
                print("Condition:4 | -3 and -4 index number(from the back) should be a .")
        else:
            print("Condition:3 | Email Address should have only one @")
    else:
        print("Condition:2 | Email Address can not have first character as number")
else:
    print("Condition:1 | Email Address can not have less than 6 characters")
